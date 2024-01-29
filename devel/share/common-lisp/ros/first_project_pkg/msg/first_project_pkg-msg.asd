
(cl:in-package :asdf)

(defsystem "first_project_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "joy" :depends-on ("_package_joy"))
    (:file "_package_joy" :depends-on ("_package"))
  ))