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

#  [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).AddCapsule

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

public int AddCapsule([Vector2](Vector2.html) vertex0, [Vector2](Vector2.html)
vertex1, float radius);

### Parameters

vertex0 | The position of one end of a capsule shape. This point represents the center point of a logical circle at the end of a capsule.  
---|---  
vertex1 | The position of the opposite end of a capsule shape. This point represents the center point of a logical circle at the opposite end of a capsule.  
radius | The radius of the capsule defining a radius around the `vertex0` and `vertex1` and the area between them.  
  
### Returns

**int** Returns the shape index the shape was added to in the
[PhysicsShapeGroup2D](PhysicsShapeGroup2D.html). This index is used as the
main reference when retrieving a shape.

### Description

Adds a capsule shape
([PhysicsShapeType2D.Capsule](PhysicsShapeType2D.Capsule.html)) to the shape
group.

A capsule shape is comprised of a single edge shape defined by two vertices
(`vertex0` and `vertex1` ) and a `radius` that extends around the length of
the edge and around the vertices.  
  
**NOTE** : A capsule forms a closed shape and does have an interior therefore
its interior is detectable by physics queries etc.

    
    
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            CreateShape();
            GetShapeFromCollider();
        }  
      
        // Create a custom shape.
        void CreateShape()
        {
            // Create a shape group.
            var shapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Add a Capsule.
            var shapeIndex = shapeGroup.AddCapsule
                (
                    vertex0: [Vector2.down](Vector2-down.html),
                    vertex1: [Vector2.up](Vector2-up.html),
                    radius: 0.5f
                );  
      
            // Fetch the actual shape created.
            var physicsShape = shapeGroup.GetShape(shapeIndex);  
      
            // Validate what we created.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Capsule](PhysicsShapeType2D.Capsule.html), physicsShape.shapeType);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.5f, physicsShape.radius);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(2, physicsShape.vertexCount);
        }  
      
        // Get a physics shape from a [Collider](Collider.html).
        void GetShapeFromCollider()
        {
            // Fetch the collider.
            var collider = GetComponent<[CapsuleCollider2D](CapsuleCollider2D.html)>();  
      
            // If the collider is not active and enabled then we'll get no shapes.
            // Let's just quit if not.
            if (!collider.isActiveAndEnabled)
                return;  
      
            // Configure the collider.
            collider.size = new [Vector2](Vector2.html)(1f, 2f);  
      
            // Create a shape group.
            var shapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Get the collider shapes.
            collider.GetShapes(shapeGroup);  
      
            // Fetch the actual shape.
            var physicsShape = shapeGroup.GetShape(0);  
      
            // Validate what we retrieved.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Capsule](PhysicsShapeType2D.Capsule.html), physicsShape.shapeType);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.5f, physicsShape.radius);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(2, physicsShape.vertexCount);
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

