[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# Touch

struct in UnityEngine

/

Implemented
in:[UnityEngine.InputLegacyModule](UnityEngine.InputLegacyModule.html)

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

Structure describing the status of a finger touching the screen.

Devices can track a number of different pieces of data about a touch on a
touchscreen, including its `phase` of the touch lifecycle, its position and
whether the touch was a single contact or several taps. Furthermore, the
continuity of a touch between frame updates can be detected by the device, so
a consistent ID number can be reported across frames and used to determine how
a particular finger is moving.  
  
The touch lifecycle describes the state of a touch in any given frame:

  * Began - A user has touched their finger to the screen this frame
  * Stationary - A finger is on the screen but the user has not moved it this frame
  * Moved - A user moved their finger this frame
  * Ended - A user lifted their finger from the screen this frame
  * Cancelled - The touch was interrupted this frame

The Touch struct is used by Unity to store data relating to a single touch
instance and is returned by the [Input.GetTouch](Input.GetTouch.html)
function. Fresh calls to GetTouch will be required on each frame update to
obtain the latest touch information from the device but the [fingerId](Touch-
fingerId.html) property can be used to identify the same touch between frames.  
  
**Note** : On iOS devices, any Touch information that is being held in memory
(for example, when you are part way through the touch lifecycle) will be lost
if the application is minimized. This happens because iOS calls ResetTouch()
and wipes all touch data from memory. The lifecycle of that touch ends there
and any functionality that relies on later phases of the touch lifecycle is
not executed. If you experience this problem, you should move the
functionality that is not being executed into
[MonoBehaviour.OnApplicationFocus](MonoBehaviour.OnApplicationFocus.html) or
[MonoBehaviour.OnApplicationPause](MonoBehaviour.OnApplicationPause.html).  
  
Additional resources: [Input.GetTouch](Input.GetTouch.html),
[TouchPhase](TouchPhase.html) enum.

### Properties

[altitudeAngle](Touch-altitudeAngle.html)| Value of 0 radians indicates that
the stylus is parallel to the surface, pi/2 indicates that it is
perpendicular.  
---|---  
[azimuthAngle](Touch-azimuthAngle.html)| Value of 0 radians indicates that the
stylus is pointed along the x-axis of the device.  
[deltaPosition](Touch-deltaPosition.html)| The position delta since last
change in pixel coordinates.  
[deltaTime](Touch-deltaTime.html)| Amount of time that has passed since the
last recorded change in Touch values.  
[fingerId](Touch-fingerId.html)| The unique index for the touch.  
[maximumPossiblePressure](Touch-maximumPossiblePressure.html)| The maximum
possible pressure value for a platform. If Input.touchPressureSupported
returns false, the value of this property will always be 1.0f.  
[phase](Touch-phase.html)| Describes the phase of the touch.  
[position](Touch-position.html)| The position of the touch in screen space
pixel coordinates.  
[pressure](Touch-pressure.html)| The current amount of pressure being applied
to a touch. 1.0f is considered to be the pressure of an average touch. If
Input.touchPressureSupported returns false, the value of this property will
always be 1.0f.  
[radius](Touch-radius.html)| An estimated value of the radius of a touch. Add
radiusVariance to get the maximum touch size, subtract it to get the minimum
touch size.  
[radiusVariance](Touch-radiusVariance.html)| This value determines the
accuracy of the touch radius. Add this value to the radius to get the maximum
touch size, subtract it to get the minimum touch size.  
[rawPosition](Touch-rawPosition.html)| The first position of the touch contact
in screen space pixel coordinates.  
[tapCount](Touch-tapCount.html)| Number of taps.  
[type](Touch-type.html)| A value that indicates whether a touch was of Direct,
Indirect (or remote), or Stylus type.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

