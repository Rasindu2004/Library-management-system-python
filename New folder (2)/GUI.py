import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import mysql.connector
from datetime import datetime, timedelta


def main_window():
    class LibraryManagementSystem:
        def __init__(self, root):
            self.root = root
            self.root.title("Library Management System")
            self.root.geometry("990x550")
            self.root.config(bg="#000000")

            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="RV118821",
                database="library"
            )
            self.cursor = self.db.cursor()

            # User Interface
            self.create_widgets()

        def create_widgets(self):
            # Title Frame
            title_frame = tk.Frame(self.root, bd=2, relief="raised", bg="#000000")
            title_frame.pack(side="top", fill="x")
            title = tk.Label(title_frame, text="LIBRARY  MANAGEMENT  SYSTEM", font=("Elephant", 20, ), bg="#000000",
                             fg="#f3f6f4")
            title.pack(pady=10)

            # Frames for different sections
            frame_user = tk.LabelFrame(self.root, text="User Management", font=("Calisto MT", 14, "bold"), bd=2, relief="ridge",
                                       bg="#cccccc")
            frame_user.place(x=20, y=80, width=950, height=200)

            frame_member = tk.LabelFrame(self.root, text="Member Management", font=("Calisto MT", 14, "bold"), bd=2,
                                         relief="ridge", bg="#cccccc")
            frame_member.place(x=20, y=190, width=950, height=200)

            frame_book = tk.LabelFrame(self.root, text="Book Management", font=("Calisto MT", 14, "bold"), bd=2, relief="ridge",
                                       bg="#cccccc")
            frame_book.place(x=20, y=300, width=950, height=200)

            frame_borrow = tk.LabelFrame(self.root, text="Borrowing Management", font=("Calisto MT", 14, "bold"), bd=2,
                                         relief="ridge", bg="#cccccc")
            frame_borrow.place(x=20, y=410, width=950, height=120)

            # User Management
            btn_add_user = tk.Button(frame_user, text="Add User", font=("Calisto MT", 12, "bold"), bg="#4caf50", fg="#222222",
                                     command=self.add_user)
            btn_add_user.grid(row=1, column=0, padx=30, pady=30)

            btn_update_user = tk.Button(frame_user, text="Update User", font=("Calisto MT", 12, "bold"), bg="#2196f3", fg="#222222",
                                        command=self.update_user)
            btn_update_user.grid(row=1, column=1, padx=30, pady=30)

            btn_delete_user = tk.Button(frame_user, text="Delete User", font=("Calisto MT", 12, "bold"), bg="#f44336", fg="#222222",
                                        command=self.delete_user)
            btn_delete_user.grid(row=1, column=2, padx=30, pady=30)

            btn_authen_user = tk.Button(frame_user, text="User Authentication", font=("Calisto MT", 12, "bold"), bg="#ff9800",
                                        fg="#222222", command=self.user_authentication)
            btn_authen_user.grid(row=1, column=3, padx=30, pady=30)

            # Member Management
            btn_add_member = tk.Button(frame_member, text="Add Member", font=("Calisto MT", 12, "bold"), bg="#4caf50", fg="#222222",
                                       command=self.add_member)
            btn_add_member.grid(row=1, column=0, padx=25, pady=30)

            btn_update_member = tk.Button(frame_member, text="Update Member", font=("Calisto MT", 12, "bold"), bg="#2196f3",
                                          fg="#222222", command=self.update_member)
            btn_update_member.grid(row=1, column=1, padx=25, pady=30)

            btn_delete_member = tk.Button(frame_member, text="Delete Member", font=("Calisto MT", 12, "bold"), bg="#f44336",
                                          fg="#222222", command=self.delete_member)
            btn_delete_member.grid(row=1, column=2, padx=25, pady=30)

            btn_view_member = tk.Button(frame_member, text="View Member details", font=("Calisto MT", 12, "bold"), bg="#ff9800",
                                        fg="#222222", command=self.view_member)
            btn_view_member.grid(row=1, column=3, padx=30, pady=30)

            btn_search_member = tk.Button(frame_member, text="Search Members", font=("Calisto MT", 12, "bold"), bg="#b700ff",
                                          fg="#222222", command=self.search_member)
            btn_search_member.grid(row=1, column=4, padx=25, pady=30)

            # Book Management
            btn_add_book = tk.Button(frame_book, text="Add Book", font=("Calisto MT", 12, "bold"), bg="#4caf50", fg="#222222",
                                     command=self.add_book)
            btn_add_book.grid(row=1, column=0, padx=25, pady=30)

            btn_update_book = tk.Button(frame_book, text="Update Book", font=("Calisto MT", 12, "bold"), bg="#2196f3", fg="#222222",
                                        command=self.update_book)
            btn_update_book.grid(row=1, column=1, padx=30, pady=30)

            btn_delete_book = tk.Button(frame_book, text="Delete Book", font=("Calisto MT", 12, "bold"), bg="#f44336", fg="#222222",
                                        command=self.delete_book)
            btn_delete_book.grid(row=1, column=2, padx=30, pady=30)

            btn_view_book = tk.Button(frame_book, text="View Book details", font=("Calisto MT", 12, "bold"), bg="#ff9800", fg="#222222",
                                      command=self.view_book)
            btn_view_book.grid(row=1, column=3, padx=30, pady=30)

            btn_search_book = tk.Button(frame_book, text="Search Books", font=("Calisto MT", 12, "bold"), bg="#b700ff", fg="#222222",
                                        command=self.search_book)
            btn_search_book.grid(row=1, column=4, padx=30, pady=30)

            # Borrowing Management
            btn_issue_book = tk.Button(frame_borrow, text="Issue Book", font=("Calisto MT", 12, "bold"), bg="#4caf50", fg="#222222",
                                       command=self.issue_book)
            btn_issue_book.grid(row=1, column=0, padx=30, pady=30)

            btn_return_book = tk.Button(frame_borrow, text="Return Book", font=("Calisto MT", 12, "bold"), bg="#2196f3", fg="#222222",
                                        command=self.return_book)
            btn_return_book.grid(row=1, column=1, padx=30, pady=30)

            btn_view_history = tk.Button(frame_borrow, text="View History", font=("Calisto MT", 12, "bold"), bg="#ff9800", fg="#222222",
                                         command=self.view_history)
            btn_view_history.grid(row=1, column=2, padx=30, pady=30)

        def add_user(self):
            def add():
                name = name_entry.get()
                address = address_entry.get()
                phone = phone_entry.get()
                role = role_entry.get()
                password = password_entry.get()
                if name and address and phone and role and password:
                    try:
                        self.cursor.execute(
                            "INSERT INTO user (name, address, phone, role, password) VALUES (%s, %s, %s, %s, %s)",
                            (name, address, phone, role, password))
                        self.db.commit()
                        self.cursor.execute("SELECT userId FROM user WHERE name = %s AND password = %s ",
                                            (name, password))
                        result = self.cursor.fetchone()

                        if result:
                            userId = result[0]
                            messagebox.showinfo("Success", f"User added successfully. Your user ID is {userId}.")
                        add_user_window.destroy()
                    except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Failed to add user: {err}")
                else:
                    messagebox.showwarning("Input Error", "Please fill all the fields")

            add_user_window = tk.Toplevel(self.root)
            add_user_window.title("Add User")
            add_user_window.geometry("300x450")
            add_user_window.config(bg="#999999")

            tk.Label(add_user_window, text="Name:",bg="#999999").pack(pady=5)
            name_entry = tk.Entry(add_user_window)
            name_entry.pack(pady=5)

            tk.Label(add_user_window, text="Address:",bg="#999999").pack(pady=5)
            address_entry = tk.Entry(add_user_window)
            address_entry.pack(pady=5)

            tk.Label(add_user_window, text="Phone Number:",bg="#999999").pack(pady=5)
            phone_entry = tk.Entry(add_user_window)
            phone_entry.pack(pady=5)

            tk.Label(add_user_window, text="Role:",bg="#999999").pack(pady=5)
            role_entry = tk.Entry(add_user_window)
            role_entry.pack(pady=5)

            tk.Label(add_user_window, text="Password:",bg="#999999").pack(pady=5)
            password_entry = tk.Entry(add_user_window, show='*')
            password_entry.pack(pady=5)

            tk.Button(add_user_window, text="Add User",bg="#3098CA", command=add).pack(pady=20)

        def update_user(self):
            def update():
                name = name_entry.get()
                address = address_entry.get()
                phone = phone_entry.get()
                role = role_entry.get()
                password = password_entry.get()
                userId = userId_entry.get()

                if userId and name and address and phone and role and password:
                    try:
                        self.cursor.execute(
                            "UPDATE user SET name = %s, address = %s, phone = %s, role = %s, password = %s where userId = %s;",
                            (name, address, phone, role, password, userId))
                        self.db.commit()
                        messagebox.showinfo("Success", "User details updated successfully")
                        update_user_window.destroy()
                    except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Failed to update the user: {err}")
                else:
                    messagebox.showwarning("Input Error", "Please fill all the fields")

            update_user_window = tk.Toplevel(self.root)
            update_user_window.title("Add User")
            update_user_window.geometry("300x450")
            update_user_window.config(bg="#999999")

            tk.Label(update_user_window, text="User ID:",bg="#999999").pack(pady=5)
            userId_entry = tk.Entry(update_user_window)
            userId_entry.pack(pady=5)

            tk.Label(update_user_window, text="Name:",bg="#999999").pack(pady=5)
            name_entry = tk.Entry(update_user_window)
            name_entry.pack(pady=5)

            tk.Label(update_user_window, text="Address:",bg="#999999").pack(pady=5)
            address_entry = tk.Entry(update_user_window)
            address_entry.pack(pady=5)

            tk.Label(update_user_window, text="Phone Number:",bg="#999999").pack(pady=5)
            phone_entry = tk.Entry(update_user_window)
            phone_entry.pack(pady=5)

            tk.Label(update_user_window, text="Role:",bg="#999999").pack(pady=5)
            role_entry = tk.Entry(update_user_window)
            role_entry.pack(pady=5)

            tk.Label(update_user_window, text="Password:",bg="#999999").pack(pady=5)
            password_entry = tk.Entry(update_user_window, show='*')
            password_entry.pack(pady=5)

            tk.Button(update_user_window, text="Update User",bg="#3098ca", command=update).pack(pady=15)

        def delete_user(self):
            def delete():
                userIdStr = userId_entry.get()
                if userIdStr:
                    try:
                        userId = int(userIdStr)
                        self.cursor.execute("DELETE FROM user WHERE userId = %s", (userId,))
                        self.db.commit()
                        messagebox.showinfo("Success", "User deleted successfully")
                        delete_user_window.destroy()
                    except ValueError:
                        messagebox.showwarning("Input Error", "User ID must be a number")
                    except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Failed to delete user: {err}")
                else:
                    messagebox.showwarning("Input Error", "Please provide a User ID")

            delete_user_window = tk.Toplevel(self.root)
            delete_user_window.title("Delete User")
            delete_user_window.geometry("300x150")
            delete_user_window.config(bg="#999999")

            tk.Label(delete_user_window, text="User ID:",bg="#999999").pack(pady=5)
            userId_entry = tk.Entry(delete_user_window)
            userId_entry.pack(pady=5)

            tk.Button(delete_user_window, text="Delete User",bg="#3098ca", command=delete).pack(pady=15)

        def user_authentication(self):
            def authenticate_user(userId, password):
                try:
                    self.cursor.execute("SELECT password FROM user WHERE userId = %s", (userId,))
                    stored_password = self.cursor.fetchone()
                    if stored_password and stored_password[0] == password:
                        return True
                    return False
                except:
                    pass

            def authen():
                userId = userId_entry.get()
                password = password_entry.get()

                if authenticate_user(userId, password):
                    messagebox.showinfo("Login", "Authentication successful!")
                    authen_user_window.destroy()
                else:
                    messagebox.showerror("Login", "Authentication failed. Please check your username and password.")

            authen_user_window = tk.Toplevel(self.root)
            authen_user_window.title("Delete User")
            authen_user_window.geometry("300x250")
            authen_user_window.config(bg="#999999")

            tk.Label(authen_user_window, text="User ID:",bg="#999999").pack(pady=5)
            userId_entry = tk.Entry(authen_user_window)
            userId_entry.pack(pady=5)

            tk.Label(authen_user_window, text="Password:",bg="#999999").pack(pady=5)
            password_entry = tk.Entry(authen_user_window, show='*')
            password_entry.pack(pady=5)

            tk.Button(authen_user_window, text="Authenticate User",bg="#3098ca", command=authen).pack(pady=15)

        def add_member(self):
            def add():
                name = name_entry.get()
                address = address_entry.get()
                phone = phone_entry.get()
                email = email_entry.get()
                if name and address and phone and email:
                    try:
                        self.cursor.execute("INSERT INTO member (name, address, phone, email) VALUES (%s, %s, %s, %s)",
                                            (name, address, phone, email))
                        self.db.commit()
                        self.cursor.execute("SELECT memberId FROM member WHERE name = %s AND email = %s ",
                                            (name, email))
                        result = self.cursor.fetchone()

                        if result:
                            memberId = result[0]
                            messagebox.showinfo("Success", f"Member added successfully. Your member ID is {memberId}.")
                        add_member_window.destroy()
                    except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Failed to add member: {err}")
                else:
                    messagebox.showwarning("Input Error", "Please fill all the fields")

            add_member_window = tk.Toplevel(self.root)
            add_member_window.title("Add member")
            add_member_window.geometry("300x400")
            add_member_window.config(bg="#999999")

            tk.Label(add_member_window, text="Name:",bg="#999999").pack(pady=5)
            name_entry = tk.Entry(add_member_window)
            name_entry.pack(pady=5)

            tk.Label(add_member_window, text="Address:",bg="#999999").pack(pady=5)
            address_entry = tk.Entry(add_member_window)
            address_entry.pack(pady=5)

            tk.Label(add_member_window, text="Phone Number:",bg="#999999").pack(pady=5)
            phone_entry = tk.Entry(add_member_window)
            phone_entry.pack(pady=5)

            tk.Label(add_member_window, text="Email:",bg="#999999").pack(pady=5)
            email_entry = tk.Entry(add_member_window)
            email_entry.pack(pady=5)

            tk.Button(add_member_window, text="Add member",bg="#3098ca", command=add).pack(pady=15)

        def update_member(self):
            def update():
                name = name_entry.get()
                address = address_entry.get()
                phone = phone_entry.get()
                email = email_entry.get()
                memberId = memberId_entry.get()

                if memberId and name and address and phone and email:
                    try:
                        self.cursor.execute(
                            "UPDATE member SET name = %s, address = %s, phone = %s, email = %s where memberId = %s;",
                            (name, address, phone, email, memberId))
                        self.db.commit()
                        messagebox.showinfo("Success", "member details updated successfully")
                        update_member_window.destroy()
                    except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Failed to update the member: {err}")
                else:
                    messagebox.showwarning("Input Error", "Please fill all the fields")

            update_member_window = tk.Toplevel(self.root)
            update_member_window.title("Add member")
            update_member_window.geometry("300x450")
            update_member_window.config(bg="#999999")

            tk.Label(update_member_window, text="member ID:",bg="#999999").pack(pady=5)
            memberId_entry = tk.Entry(update_member_window)
            memberId_entry.pack(pady=5)

            tk.Label(update_member_window, text="Name:",bg="#999999").pack(pady=5)
            name_entry = tk.Entry(update_member_window)
            name_entry.pack(pady=5)

            tk.Label(update_member_window, text="Address:",bg="#999999").pack(pady=5)
            address_entry = tk.Entry(update_member_window)
            address_entry.pack(pady=5)

            tk.Label(update_member_window, text="Phone Number:",bg="#999999").pack(pady=5)
            phone_entry = tk.Entry(update_member_window)
            phone_entry.pack(pady=5)

            tk.Label(update_member_window, text="email:",bg="#999999").pack(pady=5)
            email_entry = tk.Entry(update_member_window)
            email_entry.pack(pady=5)

            tk.Button(update_member_window, text="Update member",bg="#3098ca", command=update).pack(pady=15)

        def delete_member(self):
            def delete():
                memberIdStr = memberId_entry.get()
                if memberIdStr:
                    try:
                        memberId = int(memberIdStr)
                        self.cursor.execute("DELETE FROM member WHERE memberId = %s", (memberId,))
                        self.db.commit()
                        messagebox.showinfo("Success", "member deleted successfully")
                        delete_member_window.destroy()
                    except ValueError:
                        messagebox.showwarning("Input Error", "member ID must be a number")
                    except mysql.connector.Error as err:
                        messagebox.showerror("Error", f"Failed to delete member: {err}")
                else:
                    messagebox.showwarning("Input Error", "Please provide a member ID")

            delete_member_window = tk.Toplevel(self.root)
            delete_member_window.title("Delete member")
            delete_member_window.geometry("300x150")
            delete_member_window.config(bg="#999999")

            tk.Label(delete_member_window, text="member ID:",bg="#999999").pack(pady=5)
            memberId_entry = tk.Entry(delete_member_window)
            memberId_entry.pack(pady=5)

            tk.Button(delete_member_window, text="Delete member",bg="#3098CA", command=delete).pack(pady=10)

        def view_member(self):
            def display_member_details():
                memberId = memberId_entry.get()
                if memberId:
                    try:
                        self.cursor.execute("SELECT * FROM member WHERE memberId = %s", (memberId,))
                        member_details = self.cursor.fetchone()
                        if member_details:
                            details_window = tk.Toplevel(self.root)
                            details_window.title("Member Details")
                            details_window.geometry("300x250")
                            details_window.config(bg="#999999")

                            tk.Label(details_window, text=f"Member ID: {member_details[0]}").pack(pady=5)
                            tk.Label(details_window, text=f"Name: {member_details[1]}").pack(pady=5)
                            tk.Label(details_window, text=f"Address: {member_details[2]}").pack(pady=5)
                            tk.Label(details_window, text=f"Phone: {member_details[3]}").pack(pady=5)
                            tk.Label(details_window, text=f"Email: {member_details[4]}").pack(pady=5)
                            view_member_window.destroy()
                        else:
                            messagebox.showwarning("Not Found", "No member found with this ID")
                    except:
                        pass
                else:
                    messagebox.showwarning("Input Error", "Please provide a Member ID")

            view_member_window = tk.Toplevel(self.root)
            view_member_window.title("View Member")
            view_member_window.geometry("300x200")
            view_member_window.config(bg="#999999")

            tk.Label(view_member_window, text="Member ID:",bg="#999999").pack(pady=10)
            memberId_entry = tk.Entry(view_member_window)
            memberId_entry.pack(pady=5)
            tk.Button(view_member_window, text="Search",bg="#3098CA", command=display_member_details).pack(pady=10)

        def search_member(self):
            def perform_search():
                name = name_entry.get()
                address = address_entry.get()
                phone = phone_entry.get()
                email = email_entry.get()

                query = "SELECT * FROM member WHERE 1=1"
                params = []

                if name:
                    query += " AND name LIKE %s"
                    params.append(f"%{name}%")
                if address:
                    query += " AND address LIKE %s"
                    params.append(f"%{address}%")
                if phone:
                    query += " AND phone LIKE %s"
                    params.append(f"%{phone}%")
                if email:
                    query += " AND email LIKE %s"
                    params.append(f"%{email}%")

                try:
                    self.cursor.execute(query, tuple(params))
                    results = self.cursor.fetchall()

                    result_window = tk.Toplevel(self.root)
                    result_window.title("Search Results")
                    result_window.geometry("500x400")
                    result_window.config(bg="#999999")

                    if results:
                        for row in results:
                            tk.Label(result_window,
                                     text=f"ID:, {row[0]}, Name: {row[1]}, Address: {row[2]}, Phone: {row[3]}, Email: {row[4]}").pack(
                                pady=5)
                        search_window.destroy()
                    else:
                        tk.Label(result_window, text="No results found").pack(pady=10)

                except:
                    pass

            search_window = tk.Toplevel(self.root)
            search_window.title("Search Members")
            search_window.geometry("400x300")
            search_window.config(bg="#999999")


            tk.Label(search_window, text="Name:",bg="#999999").pack(pady=5)
            name_entry = tk.Entry(search_window)
            name_entry.pack(pady=5)

            tk.Label(search_window, text="Address:",bg="#999999").pack(pady=5)
            address_entry = tk.Entry(search_window)
            address_entry.pack(pady=5)

            tk.Label(search_window, text="Phone Number:",bg="#999999").pack(pady=5)
            phone_entry = tk.Entry(search_window)
            phone_entry.pack(pady=5)

            tk.Label(search_window, text="Email:",bg="#999999").pack(pady=5)
            email_entry = tk.Entry(search_window)
            email_entry.pack(pady=5)

            tk.Button(search_window, text="Search",bg="#3098CA", command=perform_search).pack(pady=10)

        def add_book(self):
            def add():
                title = title_entry.get()
                author = author_entry.get()
                isbn = isbn_entry.get()
                publicationYear = publicationYear_entry.get()

                if title and author and isbn and publicationYear:
                    try:
                        self.cursor.execute(
                            "INSERT INTO book (title, author, isbn, publicationYear) VALUES (%s, %s, %s, %s)",
                            (title, author, isbn, publicationYear))
                        self.db.commit()
                        self.cursor.execute("SELECT bookId FROM book WHERE title = %s AND isbn = %s ", (title, isbn))
                        result = self.cursor.fetchone()

                        if result:
                            bookId = result[0]
                            messagebox.showinfo("Success", f"Book added successfully. Your book ID is {bookId}.")
                        add_book_window.destroy()
                    except:
                        pass
                else:
                    messagebox.showwarning("Input Error", "Please fill all the fields")

            add_book_window = tk.Toplevel(self.root)
            add_book_window.title("Add book")
            add_book_window.geometry("300x400")
            add_book_window.config(bg="#999999")



            tk.Label(add_book_window, text="Title:",bg="#999999").pack(pady=5)
            title_entry = tk.Entry(add_book_window)
            title_entry.pack(pady=5)

            tk.Label(add_book_window, text="Author:",bg="#999999").pack(pady=5)
            author_entry = tk.Entry(add_book_window)
            author_entry.pack(pady=5)

            tk.Label(add_book_window, text="ISBN Number:",bg="#999999").pack(pady=5)
            isbn_entry = tk.Entry(add_book_window)
            isbn_entry.pack(pady=5)

            tk.Label(add_book_window, text="Year of publication:",bg="#999999").pack(pady=5)
            publicationYear_entry = tk.Entry(add_book_window)
            publicationYear_entry.pack(pady=5)

            tk.Button(add_book_window, text="Add book",bg="#3098ca", command=add).pack(pady=10)

        def update_book(self):
            def update():
                title = title_entry.get()
                author = author_entry.get()
                isbn = isbn_entry.get()
                publicationYear = publicationYear_entry.get()
                bookId = bookId_entry.get()

                if bookId and title and author and isbn and publicationYear:
                    try:
                        self.cursor.execute(
                            "UPDATE book SET title = %s, author = %s, isbn = %s, publicationYear = %s where bookId = %s;",
                            (title, author, isbn, publicationYear, bookId))
                        self.db.commit()
                        messagebox.showinfo("Success", "book details updated successfully")
                        update_book_window.destroy()
                    except:
                        pass
                else:
                    messagebox.showwarning("Input Error", "Please fill all the fields")

            update_book_window = tk.Toplevel(self.root)
            update_book_window.title("Add book")
            update_book_window.geometry("300x450")
            update_book_window.config(bg="#999999")

            tk.Label(update_book_window, text="Book ID:",bg="#999999").pack(pady=5)
            bookId_entry = tk.Entry(update_book_window)
            bookId_entry.pack(pady=5)

            tk.Label(update_book_window, text="Title:",bg="#999999").pack(pady=5)
            title_entry = tk.Entry(update_book_window)
            title_entry.pack(pady=5)

            tk.Label(update_book_window, text="Author:",bg="#999999").pack(pady=5)
            author_entry = tk.Entry(update_book_window)
            author_entry.pack(pady=5)

            tk.Label(update_book_window, text="ISBN Number:",bg="#999999").pack(pady=5)
            isbn_entry = tk.Entry(update_book_window)
            isbn_entry.pack(pady=5)

            tk.Label(update_book_window, text="Year of publication:",bg="#999999").pack(pady=5)
            publicationYear_entry = tk.Entry(update_book_window)
            publicationYear_entry.pack(pady=5)

            tk.Button(update_book_window, text="Update book",bg="#3098ca", command=update).pack(pady=10)

        def delete_book(self):
            def delete():
                bookIdStr = bookId_entry.get()
                if bookIdStr:
                    try:
                        bookId = int(bookIdStr)
                        self.cursor.execute("DELETE FROM book WHERE bookId = %s", (bookId,))
                        self.db.commit()
                        messagebox.showinfo("Success", "book deleted successfully")
                        delete_book_window.destroy()
                    except ValueError:
                        messagebox.showwarning("Input Error", "book ID must be a number")
                else:
                    messagebox.showwarning("Input Error", "Please provide a book ID")

            delete_book_window = tk.Toplevel(self.root)
            delete_book_window.title("Delete book")
            delete_book_window.geometry("300x150")
            delete_book_window.config(bg="#999999")

            tk.Label(delete_book_window, text="book ID:",bg="#999999").pack(pady=5)
            bookId_entry = tk.Entry(delete_book_window)
            bookId_entry.pack(pady=5)

            tk.Button(delete_book_window, text="Delete book",bg="#3098ca", command=delete).pack(pady=10)

        def view_book(self):
            def display_book_details():
                bookId = bookId_entry.get()
                if bookId:
                    try:
                        self.cursor.execute("SELECT * FROM book WHERE bookId = %s", (bookId,))
                        book_details = self.cursor.fetchone()
                        if book_details:
                            details_window = tk.Toplevel(self.root)
                            details_window.title("book Details")
                            details_window.geometry("300x250")

                            tk.Label(details_window, text=f"book ID: {book_details[0]}", bg="999999").pack(pady=5)
                            tk.Label(details_window, text=f"title: {book_details[1]}", bg="999999").pack(pady=5)
                            tk.Label(details_window, text=f"author: {book_details[2]}", bg="999999").pack(pady=5)
                            tk.Label(details_window, text=f"isbn: {book_details[3]}", bg="999999").pack(pady=5)
                            tk.Label(details_window, text=f"publicationYear: {book_details[4]}", bg="999999").pack(pady=5)
                            tk.Label(details_window, text=f"Availability: {book_details[5]}", bg="999999").pack(pady=5)
                            view_book_window.destroy()
                        else:
                            messagebox.showwarning("Not Found", "No book found with this ID")
                    except:
                        pass
                else:
                    messagebox.showwarning("Input Error", "Please provide a book ID")

            view_book_window = tk.Toplevel(self.root)
            view_book_window.title("View book")
            view_book_window.geometry("300x200")
            view_book_window.config(bg="#999999")

            tk.Label(view_book_window, text="book ID:",bg="#999999").pack(pady=10)
            bookId_entry = tk.Entry(view_book_window)
            bookId_entry.pack(pady=5)
            tk.Button(view_book_window, text="Search",bg="#3098ca", command=display_book_details).pack(pady=10)

        def search_book(self):
            def perform_search():
                title = title_entry.get()
                author = author_entry.get()
                isbn = isbn_entry.get()
                publicationYear = publicationYear_entry.get()

                query = "SELECT * FROM book WHERE 1=1"
                params = []

                if title:
                    query += " AND title LIKE %s"
                    params.append(f"%{title}%")
                if author:
                    query += " AND author LIKE %s"
                    params.append(f"%{author}%")
                if isbn:
                    query += " AND isbn LIKE %s"
                    params.append(f"%{isbn}%")
                if publicationYear:
                    query += " AND publicationYear LIKE %s"
                    params.append(f"%{publicationYear}%")

                try:
                    self.cursor.execute(query, tuple(params))
                    results = self.cursor.fetchall()

                    result_window = tk.Toplevel(self.root)
                    result_window.title("Search Results")
                    result_window.geometry("500x400")


                    if results:
                        for row in results:
                            tk.Label(result_window,
                                     text=f"ID: {row[0]}, title: {row[1]}, author: {row[2]}, isbn: {row[3]}, publicationYear: {row[4]}, Availability: {row[5]}").pack(
                                pady=5)
                        search_window.destroy()
                    else:
                        tk.Label(result_window, text="No results found").pack(pady=10)

                except:
                    pass

            search_window = tk.Toplevel(self.root)
            search_window.title("Search books")
            search_window.geometry("400x300")
            search_window.config(bg="#999999")

            tk.Label(search_window, text="Title:", bg="#999999").pack(pady=5)
            title_entry = tk.Entry(search_window)
            title_entry.pack(pady=5)

            tk.Label(search_window, text="Author:", bg="#999999").pack(pady=5)
            author_entry = tk.Entry(search_window)
            author_entry.pack(pady=5)

            tk.Label(search_window, text="ISBN Number:", bg="#999999").pack(pady=5)
            isbn_entry = tk.Entry(search_window)
            isbn_entry.pack(pady=5)

            tk.Label(search_window, text="Year of publication:", bg="#999999").pack(pady=5)
            publicationYear_entry = tk.Entry(search_window)
            publicationYear_entry.pack(pady=5)

            tk.Button(search_window, text="Search", bg="#3098ca", command=perform_search).pack(pady=10)

        def issue_book(self):
            def issue():
                bookIdStr = bookId_entry.get()
                memberId = memberId_entry.get()
                issueDate = issueDate_entry.get()

                if bookIdStr and memberId:
                    try:
                        bookId = int(bookIdStr)
                    except ValueError:
                        messagebox.showwarning("Input Error", "Invalid Book ID format")
                        return

                    if not issueDate:
                        issueDate = datetime.now().strftime("%Y-%m-%d")

                    try:
                        self.cursor.execute(
                            "INSERT INTO borrowing (bookId, memberId, issueDate) VALUES (%s, %s, %s)",
                            (bookId, memberId, issueDate))
                        self.db.commit()

                        self.cursor.execute("UPDATE book SET available = 0 WHERE bookId = %s", (bookId,))
                        self.db.commit()

                        self.cursor.execute(
                            "SELECT borrowingId FROM borrowing WHERE bookId = %s AND memberId = %s ORDER BY issueDate DESC LIMIT 1",
                            (bookId, memberId))
                        result = self.cursor.fetchone()

                        if result:
                            borrowingId = result[0]
                            messagebox.showinfo("Success", f"Book issued successfully. Your Borrowing ID is {borrowingId}.")
                        else:
                            messagebox.showwarning("Error", "Failed to retrieve borrowing ID.")

                        issue_book_window.destroy()

                    except mysql.connector.Error as err:
                        messagebox.showerror("Database Error", f"Database error: {err}")

                else:
                    messagebox.showwarning("Input Error", "Please fill all the fields")

            issue_book_window = tk.Toplevel(self.root)
            issue_book_window.title("Issue Book")
            issue_book_window.geometry("300x300")
            issue_book_window.config(bg="#999999")

            tk.Label(issue_book_window, text="Book ID:", bg="#999999").pack(pady=5)
            bookId_entry = tk.Entry(issue_book_window)
            bookId_entry.pack(pady=5)

            tk.Label(issue_book_window, text="Member ID:", bg="#999999").pack(pady=5)
            memberId_entry = tk.Entry(issue_book_window)
            memberId_entry.pack(pady=5)

            tk.Label(issue_book_window, text="Issue Date (YYYY-MM-DD, leave blank for today):", bg="#999999").pack(pady=5)
            issueDate_entry = tk.Entry(issue_book_window)
            issueDate_entry.pack(pady=5)

            tk.Button(issue_book_window, text="Issue Book", bg="#3098ca", command=issue).pack(pady=10)

        def return_book(self):
            def process_return():
                book_id = book_id_entry.get()
                member_id = member_id_entry.get()
                return_date = return_date_entry.get()

                if not (book_id and member_id and return_date):
                    messagebox.showwarning("Input Error", "Please fill in all fields.")
                    return

                try:
                    self.cursor.execute(
                        "SELECT issueDate FROM borrowing WHERE bookId = %s AND memberId = %s AND returnDate IS NULL",
                        (book_id, member_id))
                    result = self.cursor.fetchone()

                    if result:
                        issue_date = result[0]
                        if isinstance(issue_date, datetime):
                            issue_date_str = issue_date.strftime("%Y-%m-%d")
                        else:
                            issue_date_str = issue_date.isoformat()

                        # Calculate fine if the book is returned late (example: Rs.10 of fine per day after 14 days)
                        issue_date_obj = datetime.strptime(issue_date_str, "%Y-%m-%d")
                        return_date_obj = datetime.strptime(return_date, "%Y-%m-%d")
                        days_borrowed = (return_date_obj - issue_date_obj).days

                        fine = 0
                        if days_borrowed > 14:
                            fine = (days_borrowed - 14) * 10  # Assume Rs.10 fine per extra day

                        self.cursor.execute(
                            "UPDATE borrowing SET returnDate = %s, fine = %s WHERE bookId = %s AND memberId = %s AND returnDate IS NULL",
                            (return_date, fine, book_id, member_id))
                        self.db.commit()

                        self.cursor.execute("UPDATE book SET available = 1 WHERE bookId = %s", (book_id,))
                        self.db.commit()

                        messagebox.showinfo("Success", f"Book returned successfully. Fine: Rs.{fine}")
                        return_book_window.destroy()
                    else:
                        messagebox.showwarning("Not Found", "No borrowing record found for this book and member.")

                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Failed to return book: {err}")

            return_book_window = tk.Toplevel(self.root)
            return_book_window.title("Return Book")
            return_book_window.geometry("300x250")

            tk.Label(return_book_window, text="Book ID:").pack(pady=5)
            book_id_entry = tk.Entry(return_book_window)
            book_id_entry.pack(pady=5)

            tk.Label(return_book_window, text="Member ID:").pack(pady=5)
            member_id_entry = tk.Entry(return_book_window)
            member_id_entry.pack(pady=5)

            tk.Label(return_book_window, text="Return Date (YYYY-MM-DD):").pack(pady=5)
            return_date_entry = tk.Entry(return_book_window)
            return_date_entry.pack(pady=5)

            tk.Button(return_book_window, text="Return Book", command=process_return).pack(pady=10)

        def view_history(self):
            def fetch_history():
                try:
                    self.cursor.execute("SELECT * FROM borrowing")
                    results = self.cursor.fetchall()

                    history_window = tk.Toplevel(self.root)
                    history_window.title("Borrowing History")
                    history_window.geometry("700x400")

                    if results:
                        for row in results:
                            tk.Label(history_window,
                                     text=f"Borrowing ID: {row[0]}, Book ID: {row[1]}, Member ID: {row[2]}, Issue Date: {row[3]}, Return Date: {row[4]}, Fine: {row[5]}").pack(
                                pady=5)
                    else:
                        tk.Label(history_window, text="No borrowing history found.").pack(pady=10)

                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Failed to retrieve history: {err}")

            fetch_history()


    root = tk.Tk()
    app = LibraryManagementSystem(root)
    root.mainloop()
