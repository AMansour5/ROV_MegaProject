;; Auto-generated. Do not edit!


(when (boundp 'first_project_pkg::joy)
  (if (not (find-package "FIRST_PROJECT_PKG"))
    (make-package "FIRST_PROJECT_PKG"))
  (shadow 'joy (find-package "FIRST_PROJECT_PKG")))
(unless (find-package "FIRST_PROJECT_PKG::JOY")
  (make-package "FIRST_PROJECT_PKG::JOY"))

(in-package "ROS")
;;//! \htmlinclude joy.msg.html


(defclass first_project_pkg::joy
  :super ros::object
  :slots (_button_index _x _y _z _yaw _pitch ))

(defmethod first_project_pkg::joy
  (:init
   (&key
    ((:button_index __button_index) 0)
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:yaw __yaw) 0.0)
    ((:pitch __pitch) 0.0)
    )
   (send-super :init)
   (setq _button_index (round __button_index))
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _yaw (float __yaw))
   (setq _pitch (float __pitch))
   self)
  (:button_index
   (&optional __button_index)
   (if __button_index (setq _button_index __button_index)) _button_index)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:pitch
   (&optional __pitch)
   (if __pitch (setq _pitch __pitch)) _pitch)
  (:serialization-length
   ()
   (+
    ;; int32 _button_index
    4
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _z
    8
    ;; float64 _yaw
    8
    ;; float64 _pitch
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _button_index
       (write-long _button_index s)
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _z
       (sys::poke _z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _yaw
       (sys::poke _yaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _pitch
       (sys::poke _pitch (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _button_index
     (setq _button_index (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _z
     (setq _z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _yaw
     (setq _yaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _pitch
     (setq _pitch (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get first_project_pkg::joy :md5sum-) "64fd82e63708c33ce652daf7462b8e9e")
(setf (get first_project_pkg::joy :datatype-) "first_project_pkg/joy")
(setf (get first_project_pkg::joy :definition-)
      "int32 button_index
float64 x
float64 y
float64 z
float64 yaw
float64 pitch

")



(provide :first_project_pkg/joy "64fd82e63708c33ce652daf7462b8e9e")


