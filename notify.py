from win10toast import ToastNotifier 

toaster = ToastNotifier()
toaster.show_toast("Demo Notification",
                    "Hello World",
                    duration = 10)