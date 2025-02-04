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

#
[CompositeCollider2D.GeometryType](CompositeCollider2D.GeometryType.html).Outlines

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

Sets the Composite Collider 2D to generate closed outlines for the merged
collider geometry consisting of only edges.

The outline geometry is equivalent to using an
[EdgeCollider2D](EdgeCollider2D.html) with the chains of edges all connected.
While all the edges are closed (the end edge connects to the start edge),
nothing will collide in the interior of such geometry as there is no overlap
of the edges. A collision or trigger will be registered only if the edges are
in contact with a collider.  
  
This is usually the most efficient geometry to use as it produces far less
edges. Continuous edges do not cause unwanted collisions because all edges are
connected. Unwanted collisions is where two separate Colliders get in contact
even though both are aligned perfectly. Use this type of geometry to produce
platform surfaces where other Colliders are to move without any interference
from unwanted collisions.  
  
Any interior holes caused by the the composite edges surrounding it, does not
cause any interior overlap but is another closed off section of the new
Composite Collider shape.

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

