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

#  [CustomCollider2D](CustomCollider2D.html).SetCustomShape

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

public void SetCustomShape([PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)
physicsShapeGroup, int srcShapeIndex, int dstShapeIndex);

### Parameters

physicsShapeGroup | The [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html) to use as the source of shapes and vertices.  
---|---  
srcShapeIndex | The source shape index within the `physicsShapeGroup` used to assign to the Collider.  
dstShapeIndex | The destination shape index within the Collider to copy the source shape to.  
  
### Description

Sets a single shape and all associated shape vertices from the specified
`physicsShapeGroup` into the Collider.

Setting a single shape allows replacing individual shapes within the Collider.
Where possible, the Collider will reduce the amount of work required to assign
the shape. See [GetCustomShapes](CustomCollider2D.GetCustomShapes.html) for
more information on this behaviour.  
  
Any existing contacts for this Collider will be recalculated during the next
simulation step.

    
    
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Fetch the custom collider.
            var customCollider = GetComponent<[CustomCollider2D](CustomCollider2D.html)>();  
      
            // Create an input shape group.
            var inputShapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Add 5 Circles to the shape group.
            inputShapeGroup.AddCircle(center: [Vector2.zero](Vector2-zero.html),  radius: 0.5f);
            inputShapeGroup.AddCircle(center: [Vector2.zero](Vector2-zero.html),  radius: 0.6f);
            inputShapeGroup.AddCircle(center: [Vector2.zero](Vector2-zero.html),  radius: 0.7f);
            inputShapeGroup.AddCircle(center: [Vector2.zero](Vector2-zero.html),  radius: 0.8f);
            inputShapeGroup.AddCircle(center: [Vector2.zero](Vector2-zero.html),  radius: 0.9f);  
      
            // Assign our shapes.
            customCollider.SetCustomShapes(inputShapeGroup);  
      
            // Validate the contents of the custom collider.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(5, customCollider.customShapeCount);  
      
            // Transfer the last shape in the shape group to the first in the custom collider.
            customCollider.SetCustomShape(inputShapeGroup, srcShapeIndex: 4, dstShapeIndex: 0);  
      
            // Create an output shape group.
            var outputShapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Get all the custom shapes.
            var shapeCount = customCollider.GetCustomShapes(outputShapeGroup);  
      
            // Validate the results.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(5, shapeCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(5, customCollider.customShapeCount);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.9f, outputShapeGroup.GetShape(shapeIndex: 0).radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.6f, outputShapeGroup.GetShape(shapeIndex: 1).radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.7f, outputShapeGroup.GetShape(shapeIndex: 2).radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.8f, outputShapeGroup.GetShape(shapeIndex: 3).radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.9f, outputShapeGroup.GetShape(shapeIndex: 4).radius);
        }
    }
    

* * *

## Declaration

public void SetCustomShape(NativeArray<PhysicsShape2D> shapes,
NativeArray<Vector2> vertices, int srcShapeIndex, int dstShapeIndex);

### Parameters

shapes | The array to use as the source of shapes.  
---|---  
vertices | The array to use as the source of vertices.  
srcShapeIndex | The source shape index within the `shapes` array used to assign to the Collider.  
dstShapeIndex | The destination shape index within the Collider to copy the source shape to.  
  
### Description

Sets a single shape and all associated shape vertices from the specified shape
and vertices arrays into the Collider.

Setting a single shape allows replacing individual shapes within the Collider.
Where possible, the Collider will reduce the amount of work required to assign
the shape. See [GetCustomShapes](CustomCollider2D.GetCustomShapes.html) for
more information on this behaviour.  
  
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
                [0] = new [PhysicsShape2D](PhysicsShape2D.html)() { shapeType = [PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), radius = 0.5f, vertexStartIndex = 0, vertexCount = 1 },
                [1] = new [PhysicsShape2D](PhysicsShape2D.html)() { shapeType = [PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), radius = 0.6f, vertexStartIndex = 1, vertexCount = 1 },
                [2] = new [PhysicsShape2D](PhysicsShape2D.html)() { shapeType = [PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), radius = 0.7f, vertexStartIndex = 2, vertexCount = 1 },
                [3] = new [PhysicsShape2D](PhysicsShape2D.html)() { shapeType = [PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), radius = 0.8f, vertexStartIndex = 3, vertexCount = 1 },
                [4] = new [PhysicsShape2D](PhysicsShape2D.html)() { shapeType = [PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), radius = 0.9f, vertexStartIndex = 4, vertexCount = 1 },
            };  
      
            // Create a native vertices array and populate it with the vertices for the shapes.
            var vertices = new NativeArray<[Vector2](Vector2.html)>(3, [Allocator.Temp](Unity.Collections.Allocator.Temp.html))
            {
                [0] = [Vector2.zero](Vector2-zero.html),
                [1] = [Vector2.zero](Vector2-zero.html),
                [2] = [Vector2.zero](Vector2-zero.html),
                [3] = [Vector2.zero](Vector2-zero.html),
                [4] = [Vector2.zero](Vector2-zero.html),
            };  
      
            // Fetch the custom collider.
            var customCollider = GetComponent<[CustomCollider2D](CustomCollider2D.html)>();  
      
            // Assign all our test shapes.
            customCollider.SetCustomShapes(shapes, vertices);  
      
            // Assign the last shape to the first shape.
            customCollider.SetCustomShape(shapes, vertices, srcShapeIndex: 4, dstShapeIndex: 0);  
      
            // Get all the custom shapes.
            var outputShapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();
            var shapeCount = customCollider.GetCustomShapes(outputShapeGroup);  
      
            // Validate the results.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(5, shapeCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(5, customCollider.customShapeCount);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.9f, outputShapeGroup.GetShape(shapeIndex: 0).radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.6f, outputShapeGroup.GetShape(shapeIndex: 1).radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.7f, outputShapeGroup.GetShape(shapeIndex: 2).radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.8f, outputShapeGroup.GetShape(shapeIndex: 3).radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.9f, outputShapeGroup.GetShape(shapeIndex: 4).radius);
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

