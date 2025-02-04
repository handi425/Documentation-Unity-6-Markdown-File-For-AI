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

# XRNode

enumeration

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

Enumeration of XR nodes which can be updated by XR input or sent haptic data.

**Note:** The types GameController, TrackingReference, and HardwareTracker are
considered non-singleton nodes, as there can be many of each available. As a
result, InputTracking.GetLocalPosition, and InputTracking.GetLocalRotation
will not work with those values. Please use
[InputTracking.GetNodeStates](XR.InputTracking.GetNodeStates.html) instead.
**Note:** Only XR nodes with valid haptic devices as endpoints can be sent
haptic data.

### Properties

[LeftEye](XR.XRNode.LeftEye.html)| Node representing the left eye.  
---|---  
[RightEye](XR.XRNode.RightEye.html)| Node representing the right eye.  
[CenterEye](XR.XRNode.CenterEye.html)| Node representing a point between the
left and right eyes.  
[Head](XR.XRNode.Head.html)| Node representing the user's head.  
[LeftHand](XR.XRNode.LeftHand.html)| Node representing the left hand.  
[RightHand](XR.XRNode.RightHand.html)| Node representing the right hand.  
[GameController](XR.XRNode.GameController.html)| Represents a tracked game
Controller not associated with a specific hand.  
[TrackingReference](XR.XRNode.TrackingReference.html)| Represents a stationary
physical device that can be used as a point of reference in the tracked area.  
[HardwareTracker](XR.XRNode.HardwareTracker.html)| Represents a physical
device that provides tracking data for objects to which it is attached.  
  
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

