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

#  [PhysicsShapeType2D](PhysicsShapeType2D.html).Edges

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

Use multiple edges to interpret the [PhysicsShape2D](PhysicsShape2D.html)
geometry.

An edge geometry type is comprised of an unlimited quantity of vertices in the
[PhysicsShape2D](PhysicsShape2D.html) and a
[PhysicsShape2D.radius](PhysicsShape2D-radius.html). The vertices represent
the consecutive edges where each vertex connects to the next vertex. These
edges represent an open shape with no interior even if the first and last
vertices overlap. The [PhysicsShape2D.radius](PhysicsShape2D-radius.html) is
the radius of all edges. (Edges with a radius of zero become infinitely thin
edges while a radius greater than zero results in capsule shaped edges i.e.
any edge with a radius.)  
  
Edges also have an
[PhysicsShape2D.adjacentStart](PhysicsShape2D-adjacentStart.html) and
[PhysicsShape2D.adjacentEnd](PhysicsShape2D-adjacentEnd.html) feature allowing
separate edge shapes to be joined.  
  
**NOTE** : You should ensure that edges do not self-intersect as this can
produce incorrect collision responses. As checking self-intersection has a
runtime cost, this constraint is not validated and so you should ensure this
does not occur.

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

