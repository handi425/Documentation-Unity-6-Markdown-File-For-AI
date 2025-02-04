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

# XRNodeState

struct in UnityEngine.XR

/

Implemented in:[UnityEngine.XRModule](UnityEngine.XRModule.html)

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

Describes the state of a node tracked by an XR system.

To track available XR nodes and acquire state data, handle the
[InputTracking.nodeAdded](XR.InputTracking-nodeAdded.html) and
[InputTracking.nodeRemoved](XR.InputTracking-nodeRemoved.html) events or call
[InputTracking.GetNodeStates](XR.InputTracking.GetNodeStates.html).  
Not all XR platforms provide complete tracking data. Use the methods
[XRNodeState.TryGetPosition](XR.XRNodeState.TryGetPosition.html),
[XRNodeState.TryGetRotation](XR.XRNodeState.TryGetRotation.html), etc. to read
the data if it's available.  
  
XR devices can be accessed in different ways, with the XR Node representing a
physical input source such as a head position, hand, or camera.  
See [XR Input](../Manual/xr_input.html) for an overview of accessing XR
devices.

### Properties

[acceleration](XR.XRNodeState-acceleration.html)| Sets the vector representing
the current acceleration of the tracked node.  
---|---  
[angularAcceleration](XR.XRNodeState-angularAcceleration.html)| Sets the
vector representing the current angular acceleration of the tracked node.  
[angularVelocity](XR.XRNodeState-angularVelocity.html)| Sets the vector
representing the current angular velocity of the tracked node.  
[nodeType](XR.XRNodeState-nodeType.html)| The type of the tracked node as
specified in XRNode.  
[position](XR.XRNodeState-position.html)| Sets the vector representing the
current position of the tracked node.  
[rotation](XR.XRNodeState-rotation.html)| Sets the quaternion representing the
current rotation of the tracked node.  
[tracked](XR.XRNodeState-tracked.html)|  Set to true if the node is presently
being tracked by the underlying XR system, and false if the node is not
presently being tracked by the underlying XR system.  
[uniqueID](XR.XRNodeState-uniqueID.html)| The unique identifier of the tracked
node.  
[velocity](XR.XRNodeState-velocity.html)| Sets the vector representing the
current velocity of the tracked node.  
  
### Public Methods

[TryGetAcceleration](XR.XRNodeState.TryGetAcceleration.html)| Attempt to
retrieve a vector representing the current acceleration of the tracked node.  
---|---  
[TryGetAngularAcceleration](XR.XRNodeState.TryGetAngularAcceleration.html)|
Attempt to retrieve a Vector3 representing the current angular acceleration of
the tracked node.  
[TryGetAngularVelocity](XR.XRNodeState.TryGetAngularVelocity.html)| Attempt to
retrieve a Vector3 representing the current angular velocity of the tracked
node.  
[TryGetPosition](XR.XRNodeState.TryGetPosition.html)| Attempt to retrieve a
vector representing the current position of the tracked node.  
[TryGetRotation](XR.XRNodeState.TryGetRotation.html)| Attempt to retrieve a
quaternion representing the current rotation of the tracked node.  
[TryGetVelocity](XR.XRNodeState.TryGetVelocity.html)| Attempt to retrieve a
vector representing the current velocity of the tracked node.  
  
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

