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

#  [CustomCollider2D](CustomCollider2D.html).SetCustomShapes

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

public void SetCustomShapes([PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)
physicsShapeGroup);

### Parameters

physicsShapeGroup | The [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html) to use as the source of shapes and vertices.  
---|---  
  
### Description

Sets all the shapes and vertices in the Collider to those represented by the
specified [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).

All existing shapes and vertices are replaced by the shapes and vertices
contained in the specified [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).  
  
Where possible, the Collider will reduce the amount of work required to assign
the specifed shapes and vertices. The Collider checks each
[PhysicsShape2D](PhysicsShape2D.html) being assigned at each shape index and
if the Collider already contains the same physics shape then no work is done.
If the physics shape has the same [shape type](PhysicsShape2D-shapeType.html)
and [vertex count](PhysicsShape2D-vertexCount.html) then the existing physics
engine shape will only have its [radius](PhysicsShape2D-radius.html) and
[vertices](PhysicsShape2D-vertexStartIndex.html) updated. If the physics shape
has a different [shape type](PhysicsShape2D-shapeType.html) or [vertex
count](PhysicsShape2D-vertexCount.html) then the physics engine shape will be
recreated.  
  
Any existing contacts for this Collider will be recalculated during the next
simulation step.

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Fetch the custom collider.
            var customCollider = GetComponent<[CustomCollider2D](CustomCollider2D.html)>();  
      
            // Create a shape group.
            var shapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Add a Circle to the shape group.
            shapeGroup.AddCircle
                (
                    center: new [Vector2](Vector2.html)(-1f, 0f),
                    radius: 0.5f
                );  
      
            // Add a box to the shape group.
            shapeGroup.AddBox
                (
                    center: new [Vector2](Vector2.html)(1f, 0f),
                    size: new [Vector2](Vector2.html)(1f, 1f)
                );  
      
            // Assign the shapes and vertices.
            customCollider.SetCustomShapes(shapeGroup);
        }
    }
    

* * *

## Declaration

public void SetCustomShapes(NativeArray<PhysicsShape2D> shapes,
NativeArray<Vector2> vertices);

### Parameters

shapes | The array containing all the shapes used to assign to the Collider.  
---|---  
vertices | The array containing all the vertices used to assign to the Collider.  
  
### Description

Sets all the shapes and vertices in the Collider to those represented by the
specified arrays.

All existing shapes and vertices are replaced by the shapes and vertices
contained in the specified arrays.  
  
Where possible, the Collider will reduce the amount of work required to assign
the specified shapes and vertices. The Collider checks each
[PhysicsShape2D](PhysicsShape2D.html) being assigned at each shape index and
if the Collider already contains the same physics shape then no work is done.
If the physics shape has the same [shape type](PhysicsShape2D-shapeType.html)
and [vertex count](PhysicsShape2D-vertexCount.html) then the existing physics
engine shape will only have its [radius](PhysicsShape2D-radius.html) and
[vertices](PhysicsShape2D-vertexStartIndex.html) updated. If the physics shape
has a different [shape type](PhysicsShape2D-shapeType.html) or [vertex
count](PhysicsShape2D-vertexCount.html) then the physics engine shape will be
recreated.  
  
Any existing contacts for this Collider will be recalculated during the next
simulation step.

    
    
    using Unity.Collections;
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Create a native shapes array and populate it with a Circle and Capsule.
            var shapes = new NativeArray<[PhysicsShape2D](PhysicsShape2D.html)>(2, [Allocator.Temp](Unity.Collections.Allocator.Temp.html))
            {
                [0] = new [PhysicsShape2D](PhysicsShape2D.html)() { shapeType = [PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), radius = 1f, vertexStartIndex = 0, vertexCount = 1 },
                [1] = new [PhysicsShape2D](PhysicsShape2D.html)() { shapeType = [PhysicsShapeType2D.Capsule](PhysicsShapeType2D.Capsule.html), radius = 0.5f, vertexStartIndex = 1, vertexCount = 2 }
            };  
      
            // Create a native vertices array and populate it with the vertices for the shapes.
            var vertices = new NativeArray<[Vector2](Vector2.html)>(3, [Allocator.Temp](Unity.Collections.Allocator.Temp.html))
            {
                [0] = new [Vector2](Vector2.html)(2f, 3f),
                [1] = [Vector2.down](Vector2-down.html),
                [2] = [Vector2.up](Vector2-up.html)
            };  
      
            // Fetch the custom collider.
            var customCollider = GetComponent<[CustomCollider2D](CustomCollider2D.html)>();  
      
            // Set custom collider to the shapes and vertices.
            customCollider.SetCustomShapes(shapes, vertices);  
      
            // Dispose of the native arrays.
            vertices.Dispose();
            shapes.Dispose();  
      
            // Validate the collider.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(2, customCollider.customShapeCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(3, customCollider.customVertexCount);  
      
            // Get all the custom shapes.
            var shapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();
            customCollider.GetCustomShapes(shapeGroup);  
      
            // Validate the first shape and vertex.
            var shape0 = shapeGroup.GetShape(0);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), shape0.shapeType);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(1f, shape0.radius);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(0, shape0.vertexStartIndex);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1, shape0.vertexCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(new [Vector2](Vector2.html)(2f, 3f), shapeGroup.GetShapeVertex(shapeIndex: 0, vertexIndex: 0));  
      
            // Validate the second shape and vertices.
            var shape1 = shapeGroup.GetShape(1);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Capsule](PhysicsShapeType2D.Capsule.html), shape1.shapeType);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.5f, shape1.radius);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1, shape1.vertexStartIndex);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(2, shape1.vertexCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([Vector2.down](Vector2-down.html), shapeGroup.GetShapeVertex(shapeIndex: 1, vertexIndex: 0));
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([Vector2.up](Vector2-up.html), shapeGroup.GetShapeVertex(shapeIndex: 1, vertexIndex: 1));
        }
    }
    

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

