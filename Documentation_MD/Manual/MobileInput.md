[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/MobileInput.html)
  * [中文](/cn/current/Manual/MobileInput.html)
  * [日本語](/ja/current/Manual/MobileInput.html)
  * [한국어](/kr/current/Manual/MobileInput.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/MobileInput.html)
  * [中文](/cn/current/Manual/MobileInput.html)
  * [日本語](/ja/current/Manual/MobileInput.html)
  * [한국어](/kr/current/Manual/MobileInput.html)

  * [Working in Unity](working-in-unity.html)
  * [Input](Input.html)
  * [Legacy Input](InputLegacy.html)
  * Mobile device input

[](class-InputManager.html)

Input Manager

[](UIToolkits.html)

User interface (UI)

# Mobile device input  
  
---  
**Important** : This page documents part of the **Input Manager** Settings
where you can define all the different input axes, buttons and controls for
your project. [More info](class-InputManager.html)  
See in [Glossary](Glossary.html#InputManager) system, which is a legacy
feature and not recommended for new projects. **For mobile device input in new
projects you should use the[Input System Package](Input.md).**  
  
* * *

On mobile devices, the [Input](../ScriptReference/Input.html) class offers
access to touchscreen, accelerometer and geographical/location input.

Access to keyboard on mobile devices is provided via the [Mobile
keyboard](MobileKeyboard.html).

### Multi-touch screen

The iPhone, iPad and iPod Touch devices are capable of tracking up to five
fingers touching the screen simultaneously. You can retrieve the status of
each finger touching the screen during the last frame by accessing the
[Input.touches](../ScriptReference/Input-touches.html) property array.

Android devices don’t have a unified limit on how many fingers they track.
Instead, it varies from device to device and can be anything from two-touch on
older devices to five fingers on some newer devices.

Each finger touch is represented by an
[Input.Touch](../ScriptReference/Touch.html) data structure:

**_Property:_** | **_Description:_**  
---|---  
**fingerId** | The unique index for a touch.  
**position** | The screen position of the touch.  
**deltaPosition** | The screen position change since the last frame.  
**deltaTime** | Amount of time that has passed since the last state change.  
**tapCount** | The iPhone/iPad screen is able to distinguish quick finger taps by the user. This counter will let you know how many times the user has tapped the screen without moving a finger to the sides. Android devices do not count number of taps, this field is always 1.  
**phase** | Describes the state of the touch, which can help you determine whether the user has just started to touch screen, just moved their finger or just lifted their finger.  
| **Began** | A finger just touched the screen.  
| **Moved** | A finger moved on the screen.  
| **Stationary** | A finger is touching the screen but hasn’t moved since the last frame.  
| **Ended** | A finger was lifted from the screen. This is the final phase of a touch.  
| **Canceled** | The system cancelled tracking for the touch, as when (for example) the user puts the device to their face or more than five touches happened simultaneously. This is the final phase of a touch.  
  
Here’s an example script that shoots a ray whenever the user taps on the
screen:

    
    
    using UnityEngine;
    
    public class TouchInput : MonoBehaviour
    {
        GameObject particle;
    
        void Update()
        {
            foreach(Touch touch in Input.touches)
            {
                if (touch.phase == TouchPhase.Began)
                {
                    // Construct a ray from the current touch coordinates
                    Ray ray = Camera.main.ScreenPointToRay(touch.position);
                    if (Physics.Raycast(ray))
                    {
                        // Create a particle if hit
                        Instantiate(particle, transform.position, transform.rotation);
                    }
                }
            }
        }
    }
    

### Mouse simulation

On top of native touch support Unity iOS/Android provides a mouse simulation.
You can use mouse functionality from the standard
[Input](../ScriptReference/Input.html) class. Note that iOS/Android devices
are designed to support multiple finger touch. Using the mouse functionality
will support just a single finger touch. Also, finger touch on mobile devices
can move from one area to another with no movement between them. Mouse
simulation on mobile devices will provide movement, so is very different
compared to touch input. The recommendation is to use the mouse simulation
during early development but to use touch input as soon as possible.

### Accelerometer

As the mobile device moves, a built-in accelerometer reports linear
acceleration changes along the three primary axes in three-dimensional space.
Acceleration along each axis is reported directly by the hardware as G-force
values. A value of 1.0 represents a load of about +1g along a given axis while
a value of –1.0 represents –1g. If you hold the device upright (with the home
button at the bottom) in front of you, the X axis is positive along the right,
the Y axis is positive directly up, and the Z axis is positive pointing toward
you.

You can retrieve the accelerometer value by accessing the
[Input.acceleration](../ScriptReference/Input-acceleration.html) property.

The following is an example script which will move an object using the
accelerometer:

    
    
    using UnityEngine;
    
    public class Accelerometer : MonoBehaviour
    {
        float speed = 10.0f;
    
        void Update()
        {
            Vector3 dir = Vector3.zero;
            // we assume that the device is held parallel to the ground
            // and the Home button is in the right hand
    
            // remap the device acceleration axis to game coordinates:
            // 1) XY plane of the device is mapped onto XZ plane
            // 2) rotated 90 degrees around Y axis
    
            dir.x = -Input.acceleration.y;
            dir.z = Input.acceleration.x;
    
            // clamp acceleration vector to the unit sphere
            if (dir.sqrMagnitude > 1)
                dir.Normalize();
    
            // Make it move 10 meters per second instead of 10 meters per frame...
            dir *= Time.deltaTime;
    
            // Move object
            transform.Translate(dir * speed);
        }
    }
    

### Low-Pass Filter

Accelerometer readings can be jerky and noisy. Applying low-pass filtering on
the signal allows you to smooth it and get rid of high frequency noise.

The following script shows you how to apply low-pass filtering to
accelerometer readings:

    
    
    using UnityEngine;
    
    public class LowPassFilterExample : MonoBehaviour
    {
        float accelerometerUpdateInterval = 1.0f / 60.0f;
        float lowPassKernelWidthInSeconds = 1.0f;
    
        private float lowPassFilterFactor;
        private Vector3 lowPassValue = Vector3.zero;
    
        void Start()
        {
            lowPassFilterFactor = accelerometerUpdateInterval / lowPassKernelWidthInSeconds;
            lowPassValue = Input.acceleration;
        }
    
        private void Update()
        {
            lowPassValue = LowPassFilterAccelerometer(lowPassValue);
        }
    
        Vector3 LowPassFilterAccelerometer(Vector3 prevValue)
        {
            Vector3 newValue = Vector3.Lerp(prevValue, Input.acceleration, lowPassFilterFactor);
            return newValue;
        }
    }
    

The greater the value of `LowPassKernelWidthInSeconds`, the slower the
filtered value will converge towards the current input sample (and vice
versa).

### I’d like as much precision as possible when reading the accelerometer.
What should I do?

Reading the [Input.acceleration](../ScriptReference/Input-acceleration.html)
variable does not equal sampling the hardware. Put simply, Unity samples the
hardware at a frequency of 60Hz and stores the result into the variable. In
reality, things are a little bit more complicated – accelerometer sampling
doesn’t occur at consistent time intervals, if under significant CPU loads. As
a result, the system might report 2 samples during one frame, then 1 sample
during the next frame.

You can access all measurements executed by accelerometer during the frame.
The following code will illustrate a simple average of all the accelerometer
events that were collected within the last frame:

    
    
    public class AccelerationEvents : MonoBehaviour
    { 
        void Update()
        {
            GetAccelerometerValue();
        }
    
        Vector3 GetAccelerometerValue()
        {
            Vector3 acc = Vector3.zero;
            float period = 0.0f;
    
            foreach(AccelerationEvent evnt in Input.accelerationEvents)
            {
                acc += evnt.acceleration * evnt.deltaTime;
                period += evnt.deltaTime;
            }
            if (period > 0)
            {
                acc *= 1.0f / period;
            }
            return acc;
        }
    }
    

[](class-InputManager.html)

Input Manager

[](UIToolkits.html)

User interface (UI)

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

