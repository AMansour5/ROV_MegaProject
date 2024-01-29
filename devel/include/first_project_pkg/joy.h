// Generated by gencpp from file first_project_pkg/joy.msg
// DO NOT EDIT!


#ifndef FIRST_PROJECT_PKG_MESSAGE_JOY_H
#define FIRST_PROJECT_PKG_MESSAGE_JOY_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace first_project_pkg
{
template <class ContainerAllocator>
struct joy_
{
  typedef joy_<ContainerAllocator> Type;

  joy_()
    : button_index(0)
    , x(0.0)
    , y(0.0)
    , z(0.0)
    , yaw(0.0)
    , pitch(0.0)  {
    }
  joy_(const ContainerAllocator& _alloc)
    : button_index(0)
    , x(0.0)
    , y(0.0)
    , z(0.0)
    , yaw(0.0)
    , pitch(0.0)  {
  (void)_alloc;
    }



   typedef int32_t _button_index_type;
  _button_index_type button_index;

   typedef double _x_type;
  _x_type x;

   typedef double _y_type;
  _y_type y;

   typedef double _z_type;
  _z_type z;

   typedef double _yaw_type;
  _yaw_type yaw;

   typedef double _pitch_type;
  _pitch_type pitch;





  typedef boost::shared_ptr< ::first_project_pkg::joy_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::first_project_pkg::joy_<ContainerAllocator> const> ConstPtr;

}; // struct joy_

typedef ::first_project_pkg::joy_<std::allocator<void> > joy;

typedef boost::shared_ptr< ::first_project_pkg::joy > joyPtr;
typedef boost::shared_ptr< ::first_project_pkg::joy const> joyConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::first_project_pkg::joy_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::first_project_pkg::joy_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::first_project_pkg::joy_<ContainerAllocator1> & lhs, const ::first_project_pkg::joy_<ContainerAllocator2> & rhs)
{
  return lhs.button_index == rhs.button_index &&
    lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.z == rhs.z &&
    lhs.yaw == rhs.yaw &&
    lhs.pitch == rhs.pitch;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::first_project_pkg::joy_<ContainerAllocator1> & lhs, const ::first_project_pkg::joy_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace first_project_pkg

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::first_project_pkg::joy_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::first_project_pkg::joy_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::first_project_pkg::joy_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::first_project_pkg::joy_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::first_project_pkg::joy_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::first_project_pkg::joy_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::first_project_pkg::joy_<ContainerAllocator> >
{
  static const char* value()
  {
    return "64fd82e63708c33ce652daf7462b8e9e";
  }

  static const char* value(const ::first_project_pkg::joy_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x64fd82e63708c33cULL;
  static const uint64_t static_value2 = 0xe652daf7462b8e9eULL;
};

template<class ContainerAllocator>
struct DataType< ::first_project_pkg::joy_<ContainerAllocator> >
{
  static const char* value()
  {
    return "first_project_pkg/joy";
  }

  static const char* value(const ::first_project_pkg::joy_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::first_project_pkg::joy_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 button_index\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 yaw\n"
"float64 pitch\n"
;
  }

  static const char* value(const ::first_project_pkg::joy_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::first_project_pkg::joy_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.button_index);
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.z);
      stream.next(m.yaw);
      stream.next(m.pitch);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct joy_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::first_project_pkg::joy_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::first_project_pkg::joy_<ContainerAllocator>& v)
  {
    s << indent << "button_index: ";
    Printer<int32_t>::stream(s, indent + "  ", v.button_index);
    s << indent << "x: ";
    Printer<double>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
    s << indent << "z: ";
    Printer<double>::stream(s, indent + "  ", v.z);
    s << indent << "yaw: ";
    Printer<double>::stream(s, indent + "  ", v.yaw);
    s << indent << "pitch: ";
    Printer<double>::stream(s, indent + "  ", v.pitch);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FIRST_PROJECT_PKG_MESSAGE_JOY_H