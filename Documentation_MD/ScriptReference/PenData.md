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

# PenData

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

Structure describing the status of a pen event.

The PenData struct is used by Unity to store data relating to a pen event.
PenData contains information such as the position, pressure, and tilt of the
pen for a given pen input event.

### Properties

[contactType](PenData-contactType.html)| Contact type of a pen event, can be
pen up, pen down, or no contact.  
---|---  
[deltaPos](PenData-deltaPos.html)| The position delta since last pointer event
in pixel coordinates.  
[penStatus](PenData-penStatus.html)| Specifies the state of the pen. For
example, whether the pen is in contact with the screen or tablet, whether the
pen is inverted, and whether buttons are pressed.  
[position](PenData-position.html)| Specifies the position of the pen.  
[pressure](PenData-pressure.html)| How hard pen pressure is applied,
normalized between 0 (no pressure) and 1 (maximum pressure).  
[tilt](PenData-tilt.html)| Specifies the angle of the pen relative to the X
and Y axes, expressed in radians.  
[twist](PenData-twist.html)| Specifies the rotation of the pen around its
axis, expressed in radians.  
  
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

