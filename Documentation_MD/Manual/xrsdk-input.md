[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/xrsdk-input.html)
  * [中文](/cn/current/Manual/xrsdk-input.html)
  * [日本語](/ja/current/Manual/xrsdk-input.html)
  * [한국어](/kr/current/Manual/xrsdk-input.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/xrsdk-input.html)
  * [中文](/cn/current/Manual/xrsdk-input.html)
  * [日本語](/ja/current/Manual/xrsdk-input.html)
  * [한국어](/kr/current/Manual/xrsdk-input.html)

  * [Platform development ](PlatformSpecific.html)
  * [XR](XR.html)
  * [Unity XR SDK](xr-sdk.html)
  * [Subsystems](xrsdk-subsystems-landing.html)
  * XR SDK Input subsystem

[](xrsdk-subsystems-landing.html)

Subsystems

[](xrsdk-display.html)

XR SDK Display subsystem

# XR SDK Input subsystem

The **XR** An umbrella term encompassing Virtual Reality (VR), Augmented
Reality (AR) and Mixed Reality (MR) applications. Devices supporting these
forms of interactive applications can be referred to as XR devices. [More
info](XR.html)  
See in [Glossary](Glossary.html#XR) SDK Input Subsystem is an interface for
reporting button, axis, and tracking device information. This is the core
subsystem for getting user-controlled data into the various input endpoints of
the Unity engine. Unity reports your input information to
[InputDevices](../ScriptReference/XR.InputDevices.html) and the [Input
System](https://github.com/Unity-Technologies/InputSystem) depending on the
type of information available.

## Creating a basic XR Input provider

To create a basic, working XR Input provider, follow these steps:

  1. Report your device connections and disconnections
  2. Fill in all connected device’s definition information
  3. Update the device’s state whenever Unity requests this
  4. Respond to all relevant events and queries
  5. Report your device layouts to the new input system

## Terms

This guide uses the following terms:

### Devices

Most Input Subsystem APIs rely on devices. A device is a container of input
features referenced by a unique ID that you choose. This can be something
concrete, like a gamepad or headset, or it can represent abstract objects such
as a detected hand skeleton. A device has a fixed number of features that you
cannot change while the device is connected.

### Feature

Input Features are anything you can get sensor or user modified data from.
That can be a button, or a positional tracking element, or battery life. They
are grouped into various types of data, identified by UnityXRInputFeatureType.
These are the currently supported data types that can be on an input device:

**UnityXRInputFeatureType** | **Data Type**  
---|---  
kUnityXRInputFeatureTypeCustom | char[] (up to 1024 elements)  
kUnityXRInputFeatureTypeBinary | bool  
kUnityXRInputFeatureTypeDiscreteStates | unsigned int  
kUnityXRInputFeatureTypeAxis1D | float  
kUnityXRInputFeatureTypeAxis2D | UnityXRVector2  
kUnityXRInputFeatureTypeAxis3D | UnityXRVector3  
kUnityXRInputFeatureTypeRotation | UnityXRVector4  
kUnityXRInputFeatureTypeHand | UnityXRHand  
kUnityXRInputFeatureTypeBone | UnityXRBone  
kUnityXRInputFeatureTypeEyes | UnityXREyes  
  
### Usage

A usage provides context to a feature. It identifies how the developer should
use the feature. For example, the feature can be a 2D axis, but the usage
tells the developer it’s a touchpad. Usage can also inform the developer that
a one-dimensional axis feature is reporting battery life. You can create your
own usages, but you need to use as many Unity-developed usages as possible,
because they enable cross-platform utility for developers. For a list of
common usages available to all, see the Feature usages section below.

### UnityXRInternalInputDeviceId

A UnityXRInternalInputDeviceId identifies all devices. Consider these
identifiers to be unique IDs that both Unity and a provider share to reference
a specific device. You define which Ids map to which devices, with the only
constraint being that you cannot use the same Id for two devices connected at
the same time. When you report a specific Id as connecting, Unity requests
information about what the device is capable of and the current state of that
device using that Id, and sends device-specific events using that Id.

## Device connection and disconnection

Two APIs on the IUnityXRInputInterface handle device connection and
disconnection:

#### IUnityXRInputInterface.InputSubsystem_DeviceConnected

This reports a new device. The `UnityXRInternalInputDeviceId` the provider
supplies can be any value, so long as it represents an internally unique
device and no two devices are connected with the same Id from the same
provider. Devices can only be connected between the Start and Stop events of
the input provider’s lifecycle. Any device that is already connected when
**IUnityXRInputProvider.Start** is called should be reported during that
callback.

Once a device is reported as connected, Unity
calls**IUnityXRInputProvider.FillDeviceDefinition** on the next input update
loop with the supplied **UnityXRInternalInputDeviceId** in order to get
specific information about that device.

#### IUnityXRInputInterface.InputSubsystem_DeviceDisconnected

This reports that an input device is no longer available. You can only report
an input device as disconnected after you have already reported it as
connected. When you receive **IUnityXRInputProvider.Stop** , you must report
all input devices currently connected as disconnected.

The two calls above are thread safe, and can be called at any time.

## Device definitions

A Device Definition describes the features that your device can report to
Unity. Features consist of device identifying information, such as the device
name, role, manufacturer, and serial number. A Device Definition also contains
an indexed list of all individual input features available.

When a device is reported as being connected, Unity calls your provider via
**IUnityXRInputProvider.FillDeviceDefinition**. The
**UnityXRInputDeviceDefinition** parameter acts as a handle that can be passed
into any methods prefixed with **DeviceDefinition** on
**IUnityXRInputInterface**. Those methods are as follows:

### Setting identifying information

Developers use some data on the device to identify specific devices or the
general functionality of a newly connected device.

#### IUnityXRInputInterface.DeviceDefinition_SetName

This allows the provider to set the device name. The name must be clear,
succinct, and recognizable by mass market consumers. This should not include
the manufacturer’s name. This name is available to developers via
**UnityEngine.XR.InputDevice.name** and as **InputDevice.product** in the
Input System. Don’t leave this blank.

#### IUnityXRInputInterface.DeviceDefinition_SetCharacteristics

This allows the provider to specify the type of device that connected.
**UnityXRInputDeviceCharacteristics** are a series of flags that help define
what a device is capable of. These change the Input System usage of the
**InputDevice**.

#### IUnityXRInputInterface.DeviceDefinition_SetManufacturer

This allows the provider to set the manufacturer of the device. The
manufacturer must be clear, succinct, and recognizable by mass market
consumers. This string is available to developers via
**UnityEngine.XR.InputDevice.manufacturer** and as
**InputDevice.manufacturer** in the Input System. Don’t leave this blank.

#### IUnityXRInputInterface.DeviceDefinition_SetSerialNumber

This allows the provider to set the serial number of the device. This string
is available to developers via **UnityEngine.XR.InputDevice.serialNumber** and
as **InputDevice.serialNumber** in the Input System. This must be an
identifier unique to this specific device, or you should leave it blank.

### Adding Features

You can add Input Features to your device definition via the following API
calls.

#### IUnityXRInputInterface.DeviceDefinition_AddFeature

This adds a feature of a set type (except **kUnityXRInputFeatureTypeCustom**),
and returns the **UnityXRInputFeatureIndex** of that new feature.

#### IUnityXRInputInterface.DeviceDefinition_AddCustomFeature

This adds a **kUnityXRInputFeatureTypeCustom** feature. These are variable
buffers, up to 1024 bytes. You can use these to create custom types, unknown
to Unity, and require an explicit size. This method returns the
**UnityXRInputFeatureIndex** of that new feature.

#### IUnityXRInputInterface.DeviceDefinition_AddFeatureWithUsage

This adds a feature, but also includes one feature usage. This method is a
helper that combines **DeviceDefinition_AddFeature** and
**DeviceDefinition_AddUsageAtIndex** , and returns the
**UnityXRInputFeatureIndex** of that new feature.

#### IUnityXRInputInterface.DeviceDefinition_AddUsageAtIndex

This adds a feature usage to an existing feature. It takes the
**UnityXRInputFeatureIndex** from one of the methods that adds a feature. You
can add as many usages to a single feature as required.

**Note:** Returned **UnityXRInputFeatureIndex** values are all in the
sequential order they are added.

## Device states

Device states are data structures that contain the current state of the
device. The structure of the **UnityXRInputDeviceState** is described by the
**UnityXRInputDeviceDefinition**.

**Note:** Features contained within the Device State are accessed with a
**UnityXRInputFeatureIndex** as reported when declaring that feature in the
device definition.

### Device state update types

Once a definition is declared, Unity requests device states twice a frame via
**IUnityXRInputProvider.UpdateDeviceState**. The **UnityXRInputUpdateType**
parameter specifies what kind of update Unity expects:

  * **kUnityXRInputUpdateTypeDynamic** is an update before Unity iterates over **MonoBehaviour.Update** calls and coroutine continuations. These should represent where the device currently is.
  * **kUnityXRInputUpdateTypeBeforeRender** is called right before Unity prepares to render to the headset, and just before **Application.OnBeforeRender** is invoked. These calls should use a forward predicted tracking position, and represent where you’d like to render the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) at the time it takes to display it.

### Device state methods

The **UnityXRInputDeviceState** parameter acts as a handle that can be passed
into any methods prefixed with **DeviceState** on **IUnityXRInputInterface**.

#### IUnityXRInputInterface.DeviceState_SetCustomValue

This sets a feature of type **kUnityXRInputFeatureTypeCustom** at the supplied
**UnityXRInputFeatureIndex**. When setting custom value features, the provider
must always set the value with the full size of the declared feature; there is
no partial value setting. Also, you must declare all custom features to Unity
during submission with a detailed explanation of what kind of data they
contain and why they cannot exist using the other individual feature types.

#### IUnityXRInputInterface.DeviceState_SetBinaryValue

This sets a boolean (on/off) feature of type
**kUnityXRInputFeatureTypeBinary**. The default, resting, or unused state of
this feature must be false.

#### IUnityXRInputInterface.DeviceState_SetDiscreteStateValue

This sets a 32-bit unsigned integer value. This can also be used to represent
enumerations. The default, unused value must be 0, and if used for an
enumeration, 0 must represent the value of null, none, unset, or invalid.

#### IUnityXRInputInterface.DeviceState_SetAxis1DValue

This sets a 32-bit floating point value. The default, unused value must be
0.0.

#### IUnityXRInputInterface.DeviceState_SetAxis2DValue

This sets a value of type **UnityXRVector2**. UnityXRVector2 structures are a
pair of (X, Y) 32-bit floats. The default, unused value must be (0.0, 0.0).

#### IUnityXRInputInterface.DeviceState_SetAxis3DValue

This sets a value of type **UnityXRVector3**. UnityXRVector2 structures are a
pair of (X, Y, Z) 32-bit floats. The default, unused value must be (0.0, 0.0,
0.0).

#### IUnityXRInputInterface.DeviceState_SetRotationValue

This sets a value of type **UnityXRVector4** , formatted as a quaternion. The
default, unused value must be (0, 0, 0, 1). See documentation on
[quaternions](../ScriptReference/Quaternion.html)Unity’s standard way of
representing rotations as data. When writing code that deals with rotations,
you should usually use the Quaternion class and its methods. [More
info](QuaternionAndEulerRotationsInUnity.html)  
See in [Glossary](Glossary.html#Quaternion) for more information.

#### IUnityXRInputInterface.DeviceState_SetBoneValue

This sets a value of type **UnityXRBone**.

#### IUnityXRInputInterface.DeviceState_SetHandValue

This sets a value of type **UnityXRHand**.

#### IUnityXRInputInterface.DeviceState_SetEyesValue

This sets a value of type **UnityXREyes**.

**Note:** The **UnityXRInputFeatureUsageIndex** passed in is the same one
returned when adding that individual feature to the device definition when
filling out the **UnityXRInputFeatureDefinition**.

### Feature-specific structs

The following advanced types are special feature types that are used to
contain data from multiple data sources.

#### UnityXRBone

These represent a bone or one element of a hierarchical pose in space. The
**position** member represents a three-dimensional position in meters, using
left-handed coordinates where Y is up. The **rotation** member represents an
orientation in space for that bone, represented by a normalized quaternion in
radians. The **parentBoneIndex** is a **UnityXRInputFeatureIndex** that must
point to the **UnityXRBone** that is upwards in the hierarchy, or
**kUnityInvalidXRInputFeatureIndex** if it is the root for this skeleton.

#### UnityXRHand

These represent a hand-like structure of bones. They organize the bone
hierarchy into fingers and root for easy traversal. The **rootBoneIndex** must
always point to a valid index that is of type **kUnityXRInputFeatureTypeBone**
, which represents the palm or center of the hand. **fingerBoneIndices** must
be stacked such that the first dimension or the array maps to individual
fingers, following **UnityXRHandFinger** enumeration values, and the second
dimension of the array are the individual finger bones from root to tip.

#### UnityXREyes

These represent a pair of eyes, their fixation point, and current blink data.
The **leftEyePose** and **rightEyePose** are of type **UnityXRPose** , where
the **position** member represents a three-dimensional position in meters,
using left-handed coordinates, where Y is up, and the **rotation** member
represents a normalized quaternion in radians. The **fixationPoint**
represents where the left and right eyes converge, and is also a three-
dimensional position in meters, using left-handed coordinates, where Y is up.
The **leftOpenAmount** and **rightOpenAmount** represent the openness of the
eyes, where 0 is closed, and 1 is fully open. They cannot exceed the [0,1]
range.

## Event handling

Outside of device state and definition updating, Unity expects you to react
and respond to various events.

### Generic event

#### UnityXRInputProvider.HandleEvent

This is for private events, specific to this provider. The **eventType**
parameter is a custom code used to identify the payload. If the provider does
not understand that event, it must return **kUnitySubsystemErrorCodeFailure**.

### Tracking origin events

The tracking origin refers to a point in real-world space that tracked devices
are relative to. It is effectively the point in real-world space where a
device would report a position of (0, 0, 0). Unity supports a variety of
tracking origin modes, and providers can choose to opt into those that they
support. The tracking origin modes are listed under
**UnityXRInputTrackingOriginModeFlags**.

**kUnityXRInputTrackingOriginModeDevice** places the origin at the primary
device’s location and yaw at the time of startup, or at the location of the
last **UnityXRInputProvider.HandleRecenter** event.

**kUnityXRInputTrackingOriginModeFloor** places the origin somewhere on the
floor. The location on the floor is up to the provider, so long as it lets the
developer understand the height difference between the floor and various
devices.

**kUnityXRInputTrackingOriginModeTrackingReference** places the origin at the
location of a specific InputDevice with the
**kUnityXRInputDeviceCharacteristicsTrackingReference** characteristic.

Finally, **kUnityXRInputTrackingOriginModeUnknown** is an error case, and
should not be returned by the provider.

#### UnityXRInputProvider.HandleRecenter

When the tracking origin mode is set to
**kUnityXRInputTrackingOriginModeDevice** , a call to recenter should set the
current location of the primary device to be the new origin.

#### UnityXRInputProvider.QueryTrackingOriginMode

This is a request from Unity to get the current tracking origin mode that the
provider is using. The provider is expected to set the **trackingOriginMode**
parameter and return **kUnitySubsystemErrorCodeSuccess**. The returned
parameter must only be a single flag value.

#### UnityXRInputProvider.QuerySupportedTrackingOriginModes

This is a request for which tracking origin modes are supported. The provider
is expected to set the **supportedTrackingOriginModes** parameter and return
**kUnitySubsystemErrorCodeSuccess**. The returned parameter should be a
cumulative list of all **UnityXRInputTrackingOriginModeFlags** that
**UnityXRInputProvider.HandleSetTrackingOriginMode** is able to support.

#### UnityXRInputProvider.HandleSetTrackingOriginMode

This is a request from Unity to change the current tracking origin mode. The
**trackingOriginMode** parameter is the desired tracking origin mode. The
provider is expected to return **kUnitySubsystemErrorCodeSuccess** if the
origin was able to be changed, and **kUnitySubsystemErrorCodeSuccess**
otherwise. If the tracking origin mode is already the desired mode, the
provider should do nothing and return **kUnitySubsystemErrorCodeSuccess**.

#### IUnityXRInputInterface.InputSubsystem_TrackingOriginUpdated

This is an event the provider can send that notifies Unity that the location
of the tracking origin has changed. This must be called when
**UnityXRInputProvider.HandleSetTrackingOriginMode** succeeds and moves the
origin. This can also be called if the provider has had to change the origin
due to a change in overall tracking information.

#### IUnityXRInputInterface.InputSubsystem_SetTrackingBoundary

This is an event the provider can send that notifies Unity that there is a
tracking boundary available, or that the tracking boundary has changed. This
must be called if there is a boundary, and the tracking origin has changed
such that it has moved the relative position of the boundary. This can be
called with null, and 0 points in order to remove an existing tracking
boundary.

### Haptic events

#### UnityXRInputProvider.QueryHapticCapabilities

This is a request for the haptic capabilities of a given device that the
provider fills in. Setting **supportsImpulse** to true enables events for
**UnityXRInputProvider.HandleHapticImpulse**. Setting **supportsBuffer** to
true enables events for **UnityXRInputProvider.HandleHapticBuffer**.

**Note:** The capabilities structure allows the provider to set the number of
channels and requests to start and stop haptics containing a channel index.
This allows the provider to have multiple motors inside of a single device
that can be rumbled independently. The first channel should be the most common
motor to use, but subsequent ordering is provider-dependent.

#### UnityXRInputProvider.HandleHapticImpulse

This is a request for a device to rumble at a set amplitude, for a set
duration. Unity fills in the data for this request. The buffer parameter is of
type **UnityXRHapticImpulse**.

#### UnityXRInputProvider.HandleHapticBuffer

This is a request for a device to rumble a pattern, given a set buffer. Unity
fills in the data for this request. The buffer parameter is of type
**UnityXRHapticUpdate**.

The bufferSize is never more than the
**UnityXRHapticCapabilities.bufferMaxSize** returned from the
**UnityXRInputProvider.QueryHapticCapabilities** event.

#### UnityXRInputProvider.HandleHapticStop

This is a request from Unity for any haptic effects to stop. This should stop
either impulse or buffered haptic effects on the supplied
**UnityXRInternalInputDeviceId**.

## Feature Usages

Feature usages are simple string tags that provide context about your features
and help Unity developers access your device in a generic way. You can declare
your device as having a trigger, a device position, a menu button, or other
shared concept of an input feature. Developers can access these and interact
with your device without knowing exactly what it is. These are also used to
route input data into **UnityEngine.Input** and
**UnityEngine.XR.InputTracking** and decide on indices. A single input feature
can have multiple usages, but each input feature you declare must have at
least one usage assigned. If you chose to not use the usages Unity provides by
default, you must let Unity know what you’ve used when submitting for
certification, and be prepared to update your usage strings based on Unity’s
feedback.

All world space usages are in meters, m/s, m/s2, or radians where appropriate.
Space should be oriented as left-handed, z-forward, y-up. The space origin
should be the position of the device on connection. This space is your own,
and does not map directly into Unity world space.

These are the common usages available within Unity:

### Pose and tracking

The following features are for devices that supply tracking in the real world.
They are useful for identifying the current tracking capability:

**kUnityXRInputFeatureUsageIsTracked** is a boolean that specifies if the
device is currently tracking properly. True means fully tracked, false means
either partially or not tracked.

**kUnityXRInputFeatureUsageTrackingState** is a discrete state feature, backed
by the **UnityXRInputTrackingStateFlags** enumeration, that identifies which
actual tracking features are currently available and updating. This value must
never be above **kUnityXRInputTrackingStateAll**.

The remaining tracking features relay individual data about specific ‘nodes’,
such as the device, left eye, or a colour **camera** A component which creates
an image of a particular viewpoint in your scene. The output is either drawn
to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). They are grouped into sets of six,
depending on the type of data. These must be updated in conjunction with the
current value in **kUnityXRInputFeatureUsageTrackingState**. That is, if the
tracking state says position is available, all position usages must be
updating correctly.

The usage prefixes are as follows:

**Prefix** | **Description**  
---|---  
**kUnityXRInputFeatureUsageDevice** | Generalized position of the input device  
**kUnityXRInputFeatureUsageCenterEye** | Centralized average of all eye rendering locations  
**kUnityXRInputFeatureUsageLeftEye** | Rendering location for a left eye  
**kUnityXRInputFeatureUsageRightEye** | Rendering location for a right eye  
**kUnityXRInputFeatureUsageColorCamera** | Location of any incoming camera feed  
  
Each of those prefixes has a series of available suffixes that represent
various tracking attributes, and are as follows: * **Position** * **Rotation**
* **Velocity** * **AngularVelocity** * **Acceleration** *
**AngularAcceleration**

Not including these in the definition means they are never available.
Including them, but tagging them as not available via a
**kUnityXRInputFeatureUsageTrackingState** feature, means that feature is not
available currently, but could be available later.

### Device information

These contain generalized device information rather than user-actuated
controls. They are features of the device that the user does not have direct
control over.

**kUnityXRInputFeatureUsageBatteryLevel** is a 1D axis feature that represents
the current battery level of the device, where 0 is no battery, and 1 is fully
charged. It must always be within the [0–1] range.

**kUnityXRInputFeatureUsageUserPresence** is a boolean that returns true when
a user is currently wearing the headset.

### 2D axes

These are two-dimensional analog float values, such as touchpads and
joysticks. These controls are usually moved with the thumb. They provide both
an X and Y, and should always be in the range of ([–1,1],[–1,1]).

**kUnityXRInputFeatureUsagePrimary2DAxis** is a 2D axis feature that
represents a touchpad or joystick. 0,0 is the idle position and Y-positive is
away from the controller user.

**kUnityXRInputFeatureUsageSecondary2DAxis** is a 2D axis representing a
second joystick or touchpad, used in addition to
**kUnityXRInputFeatureUsagePrimary2DAxis**. 0,0 is the idle position and
Y-positive is away from the controller user.

### 1D Axes

These are all single dimensional, analog float values. Buttons, triggers, and
other controls that can be ‘half pressed’ are identified here.

**kUnityXRInputFeatureUsageTrigger** is a 1D axis that maps to an index-
actuated trigger. This must always be within the range of [0,1] where 0 is
open and 1 is fully squeezed. If this is implemented, the device must also
implement **kUnityXRInputFeatureUsageTriggerButton**.

**kUnityXRInputFeatureUsageGrip** is a 1D axis that maps to a hand squeeze
activated grip. This must always be within the range of [0,1] where 0 is open
and 1 is fully squeezed. If this is implemented, the device must also
implement **kUnityXRInputFeatureUsageGripButton**.

### Binary

These are single dimensional, digital values. They can be actuated or not, but
there is no further granularity.

**kUnityXRInputFeatureUsagePrimaryButton** is a binary feature representing
the primary button on a controller. This would commonly be used as an accept
or advance button in menus. If this is actuated, then
**kUnityXRInputFeatureUsagePrimaryTouch** must be actuated as well, if it
exists.

**kUnityXRInputFeatureUsagePrimaryTouch** is a binary feature representing the
touch state of a primary button on the controller. If this is implemented, the
device must implement **kUnityXRInputFeatureUsagePrimaryButton**.

**kUnityXRInputFeatureUsageSecondaryButton** is a binary feature representing
the secondary button on a controller. This would commonly be used as a back or
alternate button. If this is actuated, then
**kUnityXRInputFeatureUsageSecondaryTouch** must be actuated as well if it
exists.

**kUnityXRInputFeatureUsageSecondaryTouch** is a binary feature representing
the touch state of a secondary button on the controller. If this is
implemented, the device must implement
**kUnityXRInputFeatureUsageSecondaryButton**.

**kUnityXRInputFeatureUsageGripButton** is a binary feature representing
whether a hand-actuated squeeze is triggered. If this is implemented, the
device must also implement **kUnityXRInputFeatureUsageGrip**.

**kUnityXRInputFeatureUsageTriggerButton** is a boolean feature representing
whether a hand-actuated squeeze is triggered. If this is implemented, the
device must also implement **kUnityXRInputFeatureUsageTrigger**.

**kUnityXRInputFeatureUsageMenuButton** is a binary feature representing a
non-gameplay pause or menu button. This is normally not in easy reach for the
user.

**kUnityXRInputFeatureUsagePrimary2DAxisClick** is a binary feature
representing a depression or click of the
**kUnityXRInputFeatureUsagePrimary2DAxis** 2D axis. If this is implemented,
the device must implement **kUnityXRInputFeatureUsagePrimary2DAxis**. If this
is actuated, then **kUnityXRInputFeatureUsagePrimary2DAxisTouch** must be
actuated as well, if it exists.

**kUnityXRInputFeatureUsagePrimary2DAxisTouch** is a binary feature
representing a light touch of the **kUnityXRInputFeatureUsagePrimary2DAxis**
2D axis. If this is implemented, the device must implement
**kUnityXRInputFeatureUsagePrimary2DAxis**.

**kUnityXRInputFeatureUsageSecondary2DAxisClick** is a binary feature
representing a depression or click of the
**kUnityXRInputFeatureUsageSecondary2DAxis** 2D axis. If this is implemented,
the device must implement **kUnityXRInputFeatureUsageSecondary2DAxis**. If
this is actuated, then **kUnityXRInputFeatureUsageSecondary2DAxisTouch** must
be actuated as well, if it exists.

**kUnityXRInputFeatureUsageSecondary2DAxisTouch** is a binary feature
representing a light touch of the **kUnityXRInputFeatureUsageSecondary2DAxis**
2D axis. If this is implemented, the device must implement
**kUnityXRInputFeatureUsageSecondary2DAxis**.

### Sensor Based

These represent individual sensor types. They are used as shorthand to search
for hand and eye type data.

**kUnityXRInputFeatureUsageHandData** is a **UnityXRHands** feature
representing hand tracking data. **kUnityXRInputFeatureUsageEyesData** is a
**UnityXREyes** feature representing eye tracking data.

# New Input System device layouts

To enable users to bind to and use code to access your device properties when
using the new Input System, you need to provide device layout descriptions as
part of your input provider.

You should provide a device layout for each device type you define in the
input provider. If you don’t provide an explicit device layout for a device
you register, users won’t be able to use the new Input System **UI**(User
Interface) Allows a user to interact with your application. Unity currently
supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) to bind to features on your device. The
Input System will still receive device data, and users will be able to
manually create bindings to your new device features.

For more information on Input System device layouts, see the Input System
[documentation](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.0/manual/Layouts.html).
An example is provided below for ease of implementation.

## Example device layout

This example provides a layout for a new Example **VR** Virtual Reality [More
info](VROverview.html)  
See in [Glossary](Glossary.html#VR) Controller. The Example VR Controller’s
XRSDK layout definition is described as having: \- An Additional
`kUnityXRInputFeatureTypeBinary` which is called `exampleButton` \- A
`kUnityXRInputFeatureTypeAxis3D` value called `examplePosition` \- A
`kUnityXRInputFeatureTypeRotation` value called `exampleRotation`

To allow users to bind and control the device using the new Input System, you
must provide a device layout for your new Example VR Controller.

First, you need to provide an `InputControlLayout` attribute, and also provide
an explicit name for use with the New Input System UI. Use the `[Preseve]`
attribute to ensure that these elements are not stripped from the compilation
step.

    
    
    [Preserve]
    [InputControlLayout(displayName = "Example VR Controller")]
    public class ExampleVRController : XRController
    {
    

Next, provide `InputControl` mappings for the various elements defined in the
XRSDK Layout. Use `[Preserve]` again to ensure that these elements are not
stripped from the build. The use of the `aliases` keyword allows the new Input
System to perform common matching based on the aliases you provide.

    
    
            [Preserve]
            [InputControl(aliases = new[] { "PrimaryButton" })]
            public ButtonControl exampleButton { get; private set; }
            [Preserve]
            [InputControl]
            public Vector3Control examplePosition { get; private set; }
            [Preserve]
            [InputControl]
            public QuaternionControl exampleRotation { get; private set; }
    

Finally, provide an implementation of the `FinishSetup` method which binds the
control mapping to the instance of the control. Ensure you also call the base
class’s `FinishSetup`, otherwise the base controls are not bound.

    
    
            protected override void FinishSetup()
            {
                base.FinishSetup();
    
                exampleButton = GetChildControl<ButtonControl>("exampleButton");
                examplePosition = GetChildControl<Vector3Control>("examplePosition");
                exampleRotation = GetChildControl<QuaternionControl>("exampleRotation");            
            }
    
    

## Registering your layouts

The last step you need to perform is to register the new device layouts with
the New Input System when you start the XRSDK Loader for these devices. The
following code is an example of this implementation.

You must fill out the `REGEX THAT MATCHES YOUR DEVICE` section with the
correct matching strings to the product, or other strings provided by your
XRSDK Input Provider when the device is connected.

    
    
            public override bool Initialize()
            {
    #if UNITY_INPUT_SYSTEM
                InputLayoutLoader.RegisterInputLayouts();
    #endif
    
    #if UNITY_INPUT_SYSTEM
    #if UNITY_EDITOR
        [InitializeOnLoad]
    #endif
        static class InputLayoutLoader
        {
            static InputLayoutLoader()
            {
                RegisterInputLayouts();
            }
    
            public static void RegisterInputLayouts()
            {
                UnityEngine.InputSystem.InputSystem.RegisterLayout<ExampleVRController>(
                    matches: new InputDeviceMatcher()
                        .WithInterface(XRUtilities.InterfaceMatchAnyVersion)
                        .WithProduct("<REGEX THAT MATCHES YOUR DEVICE>")
                );
    
    

* * *

## Checklist for creating your own input provider

  * Set up basic lifecycle registration: 
    * **IUnityXRInputInterface.RegisterLifecycleProvider** with function pointers for Initialize, Start, Stop, Shutdown.
    * **IUnityXRInputInterface.RegisterInputProvider** called from **UnityLifecycleProvider.Initialize** callback with Input Provider calls filled out.
  * Call **IUnityXRInputInterface.InputSubsystem_DeviceConnected** with a unique Id for each connected device.
  * Fill out valid device definitions for each device in **UnityXRInputProvider.FillDeviceDefinition** : 
    * Add a valid name.
    * Add a valid role.
    * Add at least one Input Feature.
  * Update the device state in **UnityXRInputProvider.UpdateDeviceState** for each connected device. 
    * If you can forward predict tracking positions for rendering, do so when an update is of type **kUnityXRInputUpdateTypeBeforeRender**.
  * Call **IUnityXRInputInterface.InputSubsystem_SetBoundaryPoints** with any bounding box.
  * Implement **UnityXRInputProvider.QueryTrackingOriginMode** , **UnityXRInputProvider.QuerySupportedTrackingOriginModes** , and **UnityXRInputProvider.HandleSetTrackingOriginMode**.
  * Implement **UnityXRInputProvider.TryRecenter**.
  * Provide new Input System device layouts for your devices.

[](xrsdk-subsystems-landing.html)

Subsystems

[](xrsdk-display.html)

XR SDK Display subsystem

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

