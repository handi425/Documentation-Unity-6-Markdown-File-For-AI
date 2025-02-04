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

# SystemGestureDeferMode

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

Bit-mask used to control the deferring of system gestures on iOS.

On iPhone X the home button is implemented as a system gesture (swipe up from
the lower edge of the screen). Other gestures are implemented as swipes from
other screen edges. Note, this may interfere with games that use swipes as an
interaction method. This bit-mask specifies which screen edge gestures the
system defers to the second swipe. If deferring is enabled on a specific
screen edge, the first swipe is ignored and provides a way to reduce unwanted
interactions with the App. Note that iOS Human interface guidelines do not
recommend enabling this behavior as it may confuse users.

### Properties

[None](iOS.SystemGestureDeferMode.None.html)| Disables gesture deferring on
all edges.  
---|---  
[TopEdge](iOS.SystemGestureDeferMode.TopEdge.html)| Identifies top screen
edge.  
[LeftEdge](iOS.SystemGestureDeferMode.LeftEdge.html)| Identifies left screen
edge.  
[BottomEdge](iOS.SystemGestureDeferMode.BottomEdge.html)| Identifies bottom
screen edge.  
[RightEdge](iOS.SystemGestureDeferMode.RightEdge.html)| Identifies right
screen edge.  
[All](iOS.SystemGestureDeferMode.All.html)| Identifies all screen edges.  
  
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

