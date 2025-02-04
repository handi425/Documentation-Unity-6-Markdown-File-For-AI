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

#  [Rigidbody2D](Rigidbody2D.html).GetShapes

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

public int GetShapes([PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)
physicsShapeGroup);

### Parameters

physicsShapeGroup | The [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html) to store the retrieved [PhysicsShape2D](PhysicsShape2D.html) in.  
---|---  
  
### Returns

**int** Returns the number of [PhysicsShape2D](PhysicsShape2D.html) retrieved
from the [Rigidbody2D](Rigidbody2D.html).

### Description

Gets all the [PhysicsShape2D](PhysicsShape2D.html) used by all
[Collider2D](Collider2D.html) attached to the [Rigidbody2D](Rigidbody2D.html).

Where [Collider2D.GetShapes](Collider2D.GetShapes.html) will retrieve all
shapes used by a specific [Collider2D](Collider2D.html), this method will
return all the shapes on all [Collider2D](Collider2D.html) attached to the
[Rigidbody2D](Rigidbody2D.html).  
  
For a complete description of how retrieving shapes works, refer to
[Collider2D.GetShapes](Collider2D.GetShapes.html).

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

