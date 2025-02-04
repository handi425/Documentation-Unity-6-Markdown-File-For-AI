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

**Method group is Obsolete**  

#  [InputTracking](XR.InputTracking.html).GetLocalRotation

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

**Obsolete** This API is obsolete, and should no longer be used. Please use
InputDevice.TryGetFeatureValue with the CommonUsages.deviceRotation usage
instead.

## Declaration

public static [Quaternion](Quaternion.html)
GetLocalRotation([XR.XRNode](XR.XRNode.html) node);

### Parameters

node | Specifies which node's rotation should be returned.  
---|---  
  
### Returns

**Quaternion** The rotation of the node in its local tracking space.

### Description

**Note** : This API has been marked as obsolete in code, and is no longer in
use. Please use
[InputTracking.GetNodeStates](XR.InputTracking.GetNodeStates.html) and look
for the [XRNodeState](XR.XRNodeState.html) with the corresponding
[XRNode](XR.XRNode.html) type instead. Gets the rotation of a specific node.

This can be used to keep objects at the same orientation as the given node.
For example, if the user picks up an object you can use this method along with
InputTracking.GetLocalPosition to ensure the object is correctly positioned
and oriented to match the user's hand.  
  
**Note:** This function doesn't work with the following XRNode types:
GameController, TrackingReference, or HardwareTracker. Use the
[InputTracking.GetNodeStates](XR.InputTracking.GetNodeStates.html) method
instead. See [XRNode](XR.XRNode.html) for more details.

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

