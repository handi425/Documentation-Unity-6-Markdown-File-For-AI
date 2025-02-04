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

#  [Rigidbody2D](Rigidbody2D.html).MovePositionAndRotation

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

## Declaration

public void MovePositionAndRotation([Vector2](Vector2.html) position, float
angle);

### Parameters

position | The position to move the rigidbody to.  
---|---  
angle | The angle to move the rigidbody to.  
  
### Description

Moves the rigidbody position to `position` and the rigidbody angle to `angle`.

This is a combination of calling both
[MovePosition](Rigidbody2D.MovePosition.html) and
[MoveRotation](Rigidbody2D.MoveRotation.html). This can be used to increase
performance by not having to perform two separate calls to queue movements.  
  
For more details on the operation of movement using these methods, refer to
[Rigidbody2D.MovePosition](Rigidbody2D.MovePosition.html) and
[Rigidbody2D.MoveRotation](Rigidbody2D.MoveRotation.html).

* * *

## Declaration

public void MovePositionAndRotation([Vector2](Vector2.html) position,
[Quaternion](Quaternion.html) rotation);

### Parameters

position | The position to move the rigidbody to.  
---|---  
rotation | The rotation to move the rigidbody to. Only the Z-Axis rotation is used from the full 3D Quaternion rotation.  
  
### Description

Moves the rigidbody position to `position` and the rigidbody angle to
`rotation`.

This is a combination of calling both
[MovePosition](Rigidbody2D.MovePosition.html) and
[MoveRotation](Rigidbody2D.MoveRotation.html). This can be used to increase
performance by not having to perform two separate calls to queue movements.  
  
For more details on the operation of movement using these methods, refer to
[Rigidbody2D.MovePosition](Rigidbody2D.MovePosition.html) and
[Rigidbody2D.MoveRotation](Rigidbody2D.MoveRotation.html).

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

