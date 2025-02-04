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

#  [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).GetShapeData

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

public void GetShapeData(List<PhysicsShape2D> shapes, List<Vector2> vertices);

### Parameters

shapes | A list that will be populated with a copy of all the shapes in the [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).  
---|---  
vertices | A list that will be populated with a copy of all the vertices in the [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).  
  
### Description

Gets a copy of both the shapes and vertices in the
[PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).

**NOTE** : Because this is a copy, changing the specified `shapes` and
`vertices` lists afterwards will not change the
[PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).

    
    
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Create a shape group.
            var shapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Add a Circle to the shape group.
            var circleShapeIndex = shapeGroup.AddCircle
                (
                    center: new [Vector2](Vector2.html)(-2f, 3f),
                    radius: 1f
                );  
      
            // Add a Capsule to the shape group.
            var capsuleShapeIndex = shapeGroup.AddCapsule
                (
                    vertex0: [Vector2.down](Vector2-down.html),
                    vertex1: [Vector2.up](Vector2-up.html),
                    radius: 0.5f
                );  
      
            // Validate the contents.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), shapeGroup.GetShape(circleShapeIndex).shapeType);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Capsule](PhysicsShapeType2D.Capsule.html), shapeGroup.GetShape(capsuleShapeIndex).shapeType);  
      
            // Fetch the shapes and vertices from the shape group.
            var shapes = new List<[PhysicsShape2D](PhysicsShape2D.html)>();
            var vertices = new List<[Vector2](Vector2.html)>();
            shapeGroup.GetShapeData(shapes, vertices);  
      
            // Fetch the Circle shape and validate shape and vertex.
            var circleShape = shapes[circleShapeIndex];
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), circleShape.shapeType);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(1f, circleShape.radius);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(new [Vector2](Vector2.html)(-2f, 3f), vertices[circleShape.vertexStartIndex]);  
      
            // Fetch the Capsule shape and validate shape and vertices (2).
            var capsuleShape = shapes[capsuleShapeIndex];
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Capsule](PhysicsShapeType2D.Capsule.html), capsuleShape.shapeType);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.5f, capsuleShape.radius);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([Vector2.down](Vector2-down.html), vertices[capsuleShape.vertexStartIndex]);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([Vector2.up](Vector2-up.html), vertices[capsuleShape.vertexStartIndex + 1]);
        }
    }
    

* * *

## Declaration

public void GetShapeData(NativeArray<PhysicsShape2D> shapes,
NativeArray<Vector2> vertices);

### Parameters

shapes | A NativeArray that will be populated with a copy of all the shapes in the [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).  
---|---  
vertices | A NativeArray that will be populated with a copy of all the vertices in the [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).  
  
### Description

Gets a copy of both the shapes and vertices in the
[PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).

**NOTE** : Because this is a copy, changing the specified `shapes` and
`vertices` arrays afterwards will not change the
[PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).

    
    
    using Unity.Collections;
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Create a shape group.
            var shapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Add a Circle to the shape group.
            var circleShapeIndex = shapeGroup.AddCircle
                (
                    center: new [Vector2](Vector2.html)(-2f, 3f),
                    radius: 1f
                );  
      
            // Add a Capsule to the shape group.
            var capsuleShapeIndex = shapeGroup.AddCapsule
                (
                    vertex0: [Vector2.down](Vector2-down.html),
                    vertex1: [Vector2.up](Vector2-up.html),
                    radius: 0.5f
                );  
      
            // Validate the contents.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), shapeGroup.GetShape(circleShapeIndex).shapeType);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Capsule](PhysicsShapeType2D.Capsule.html), shapeGroup.GetShape(capsuleShapeIndex).shapeType);  
      
            // Fetch the shapes and vertices from the shape group.
            var shapes = new NativeArray<[PhysicsShape2D](PhysicsShape2D.html)>(shapeGroup.shapeCount, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            var vertices = new NativeArray<[Vector2](Vector2.html)>(shapeGroup.vertexCount, [Allocator.Temp](Unity.Collections.Allocator.Temp.html));
            shapeGroup.GetShapeData(shapes, vertices);  
      
            // Fetch the Circle shape and validate shape and vertex.
            var circleShape = shapes[circleShapeIndex];
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), circleShape.shapeType);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(1f, circleShape.radius);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(new [Vector2](Vector2.html)(-2f, 3f), vertices[circleShape.vertexStartIndex]);  
      
            // Fetch the Capsule shape and validate shape and vertices (2).
            var capsuleShape = shapes[capsuleShapeIndex];
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Capsule](PhysicsShapeType2D.Capsule.html), capsuleShape.shapeType);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.5f, capsuleShape.radius);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([Vector2.down](Vector2-down.html), vertices[capsuleShape.vertexStartIndex]);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([Vector2.up](Vector2-up.html), vertices[capsuleShape.vertexStartIndex + 1]);  
      
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

