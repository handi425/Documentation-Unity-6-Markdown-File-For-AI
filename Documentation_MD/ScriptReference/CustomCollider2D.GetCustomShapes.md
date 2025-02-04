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

#  [CustomCollider2D](CustomCollider2D.html).GetCustomShapes

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

public int GetCustomShapes([PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)
physicsShapeGroup);

### Parameters

physicsShapeGroup | The physics shape group that will receive all the [physics shapes](PhysicsShape2D.html) and [vertices](Vector2.html) from the Collider.  
---|---  
  
### Returns

**int** Returns the total number of [physics shapes](PhysicsShape2D.html)
placed in the specified `physicsShapeGroup`.

### Description

Gets all the physics shapes and vertices in the Collider and places them in
the specified [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).

    
    
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
      
            // Create an output shape group.
            var outputShapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Get all the custom shapes.
            var shapeCount = customCollider.GetCustomShapes(outputShapeGroup);  
      
            // Validate the results.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(5, shapeCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(5, outputShapeGroup.shapeCount);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.5f, outputShapeGroup.GetShape(shapeIndex: 0).radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.6f, outputShapeGroup.GetShape(shapeIndex: 1).radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.7f, outputShapeGroup.GetShape(shapeIndex: 2).radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.8f, outputShapeGroup.GetShape(shapeIndex: 3).radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.9f, outputShapeGroup.GetShape(shapeIndex: 4).radius);
        }
    }
    

* * *

## Declaration

public int GetCustomShapes([PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)
physicsShapeGroup, int shapeIndex, int shapeCount = 1);

### Parameters

physicsShapeGroup | The physics shape group that will receive the [physics shapes](PhysicsShape2D.html) and [vertices](Vector2.html) from the Collider.  
---|---  
shapeIndex | The shape index within the Collider to start retrieving shapes from.  
shapeCount | The total number of shapes starting at the `shapeIndex` to retrieve.  
  
### Returns

**int** The total number of [physics shapes](PhysicsShape2D.html) placed in
the specified `physicsShapeGroup`.

### Description

Gets a specified number of physics shapes defined by`shapeCount` starting at
`shapeIndex` along with all associated vertices those shapes use and places
them in the specified [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).

    
    
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
      
            // Create an output shape group.
            var outputShapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Get the last 3 custom shapes.
            var shapeCount = customCollider.GetCustomShapes(outputShapeGroup, shapeIndex: 2, shapeCount: 3);  
      
            // Validate the results.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(3, shapeCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(3, outputShapeGroup.shapeCount);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.7f, outputShapeGroup.GetShape(shapeIndex: 0).radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.8f, outputShapeGroup.GetShape(shapeIndex: 1).radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.9f, outputShapeGroup.GetShape(shapeIndex: 2).radius);
        }
    }
    

* * *

## Declaration

public int GetCustomShapes(NativeArray<PhysicsShape2D> shapes,
NativeArray<Vector2> vertices);

### Parameters

shapes | The array that will be populated with a copy of all the shapes in the [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).  
---|---  
vertices | The array that will be populated with a copy of all the vertices in the [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).  
  
### Returns

**int** Returns the total number of [physics shapes](PhysicsShape2D.html)
placed in the specified arrays.

### Description

Gets all the physics shapes and vertices in the Collider and places them in
the specified arrays.

    
    
    using Unity.Collections;
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
            inputShapeGroup.AddCircle(center: new [Vector2](Vector2.html)(3f, 8f), radius: 0.5f);
            inputShapeGroup.AddCircle(center: new [Vector2](Vector2.html)(6f, 3f), radius: 0.6f);
            inputShapeGroup.AddCircle(center: new [Vector2](Vector2.html)(2f, 5f), radius: 0.7f);
            inputShapeGroup.AddCircle(center: new [Vector2](Vector2.html)(9f, 2f), radius: 0.8f);
            inputShapeGroup.AddCircle(center: new [Vector2](Vector2.html)(1f, 7f), radius: 0.9f);  
      
            // Assign our shapes.
            customCollider.SetCustomShapes(inputShapeGroup);  
      
            // Validate the contents of the custom collider.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(5, customCollider.customShapeCount);  
      
            // Get all the custom shapes.
            var shapes = new NativeArray<[PhysicsShape2D](PhysicsShape2D.html)>(customCollider.customShapeCount, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            var vertices = new NativeArray<[Vector2](Vector2.html)>(customCollider.customVertexCount, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            var shapeCount = customCollider.GetCustomShapes(shapes, vertices);  
      
            // Validate the shapes.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(5, shapeCount);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.5f, shapes[0].radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.6f, shapes[1].radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.7f, shapes[2].radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.8f, shapes[3].radius);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.9f, shapes[4].radius);  
      
            // Validate the vertices.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(new [Vector2](Vector2.html)(3f, 8f), vertices[0]);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(new [Vector2](Vector2.html)(6f, 3f), vertices[1]);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(new [Vector2](Vector2.html)(2f, 5f), vertices[2]);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(new [Vector2](Vector2.html)(9f, 2f), vertices[3]);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(new [Vector2](Vector2.html)(1f, 7f), vertices[4]);  
      
            // Dispose of the native arrays.
            vertices.Dispose();
            shapes.Dispose();
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

