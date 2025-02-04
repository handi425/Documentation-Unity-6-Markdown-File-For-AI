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

# PhysicsShapeGroup2D

class in UnityEngine

/

Implemented in:[UnityEngine.Physics2DModule](UnityEngine.Physics2DModule.html)

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

Represents a group of [PhysicsShape2D](PhysicsShape2D.html) and their
geometry.

A shape group represents multiple [PhysicsShape2D](PhysicsShape2D.html) of the
same or mixed [PhysicsShapeType2D](PhysicsShapeType2D.html) along with their
geometry. It is comprised of a single list of vertices
([GetShapeVertices](PhysicsShapegroup2D.GetShapeVertices.html)) along with a
list of [PhysicsShape2D](PhysicsShape2D.html) which refer to specific ranges
of those vertices i.e. they index into the list of vertices. Some shape types
([PhysicsShapeType2D](PhysicsShapeType2D.html)) use a fixed number of vertices
and some use a variable number of vertices therefore this single vertices list
is a compact and efficient representation for multiple
[PhysicsShape2D](PhysicsShape2D.html) in a group.  
  
The shape group can be created by using the following methods:

  * Calling [Collider2D.GetShapes](Collider2D.GetShapes.html) where it would then represent all the shapes produced by that [Collider2D](Collider2D.html)
  * Calling [Rigidbody2D.GetShapes](Rigidbody2D.GetShapes.html) where it would then represent all the shapes produced by all the[Collider2D](Collider2D.html) attached to that [Rigidbody2D](Rigidbody2D.html)
  * Manually populating with custom shapes by calling [AddCircle](PhysicsShapeGroup2D.AddCircle.html), [AddCapsule](PhysicsShapeGroup2D.AddCapsule.html), [AddPolygon](PhysicsShapeGroup2D.AddPolygon.html), [AddBox](PhysicsShapeGroup2D.AddBox.html) or [AddEdges](PhysicsShapeGroup2D.AddEdges.html).

### Properties

[localToWorldMatrix](PhysicsShapeGroup2D-localToWorldMatrix.html)| Gets or
sets a matrix that transforms the PhysicsShapeGroup2D vertices from local
space into world space.  
---|---  
[shapeCount](PhysicsShapeGroup2D-shapeCount.html)| The total number of
PhysicsShape2D in the shape group. (Read Only)  
[vertexCount](PhysicsShapeGroup2D-vertexCount.html)| The total number of
vertices in the shape group used to represent all PhysicsShape2D within it.
(Read Only)  
  
### Constructors

[PhysicsShapeGroup2D](PhysicsShapeGroup2D-ctor.html)| Initializes and returns
an instance of PhysicsShapeGroup2D. The shape group will be empty and ready
for use by Collider2D.GetShapes, Rigidbody2D.GetShapes or manually adding
shapes.  
---|---  
  
### Public Methods

[Add](PhysicsShapeGroup2D.Add.html)| Adds a copy of all the PhysicsShape2D and
their geometry from the specified physicsShapeGroup into this shape group. The
specified physicsShapeGroup is not modified.  
---|---  
[AddBox](PhysicsShapeGroup2D.AddBox.html)| Adds a box shape
(PhysicsShapeType2D.Polygon) to the shape group.  
[AddCapsule](PhysicsShapeGroup2D.AddCapsule.html)| Adds a capsule shape
(PhysicsShapeType2D.Capsule) to the shape group.  
[AddCircle](PhysicsShapeGroup2D.AddCircle.html)| Adds a circle shape
(PhysicsShapeType2D.Circle) to the shape group.  
[AddEdges](PhysicsShapeGroup2D.AddEdges.html)| Adds an edges shape
(PhysicsShapeType2D.Edges) to the shape group.  
[AddPolygon](PhysicsShapeGroup2D.AddPolygon.html)| Adds a polygon shape
(PhysicsShapeType2D.Polygon) to the shape group.  
[Clear](PhysicsShapeGroup2D.Clear.html)| Clears all the vertices and shapes
from the PhysicsShapeGroup.  
[DeleteShape](PhysicsShapeGroup2D.DeleteShape.html)| When destroying a shape
at the specified shapeIndex, all other shapes that exist above the specified
shapeIndex will have their shape indices updated appropriately.  
[GetShape](PhysicsShapeGroup2D.GetShape.html)| Gets the PhysicsShape2D stored
at the specified shapeIndex.  
[GetShapeData](PhysicsShapeGroup2D.GetShapeData.html)| Gets a copy of both the
shapes and vertices in the PhysicsShapeGroup2D.  
[GetShapeVertex](PhysicsShapeGroup2D.GetShapeVertex.html)| Gets a single
vertex of a shape. The vertex index is zero-based with the shape having a
quantity of vertex specified by PhysicsShape2D.vertexCount.  
[GetShapeVertices](PhysicsShapeGroup2D.GetShapeVertices.html)| Gets a copy of
the shape vertices in the PhysicsShapeGroup2D.  
[SetShapeAdjacentVertices](PhysicsShapeGroup2D.SetShapeAdjacentVertices.html)|
Sets the adjacent vertices of a shape.  
[SetShapeRadius](PhysicsShapeGroup2D.SetShapeRadius.html)| Sets the radius of
a shape.  
[SetShapeVertex](PhysicsShapeGroup2D.SetShapeVertex.html)| Sets a single
vertex of a shape.  
  
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

