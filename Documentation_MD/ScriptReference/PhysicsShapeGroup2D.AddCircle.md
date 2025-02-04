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

#  [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).AddCircle

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

public int AddCircle([Vector2](Vector2.html) center, float radius);

### Parameters

center | The center point of the circle shape. This is analogous to [Collider2D.offset](Collider2D-offset.html).  
---|---  
radius | The radius of the circle defining a radius around the `center`. This is identical to [CircleCollider2D.radius](CircleCollider2D-radius.html).  
  
### Returns

**int** Returns the shape index the shape was added to in the
[PhysicsShapeGroup2D](PhysicsShapeGroup2D.html). This index is used as the
main reference when retrieving a shape.

### Description

Adds a circle shape
([PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html)) to the shape
group.

A circle shape is comprised of a single vertex (`center` ) and a `radius` that
extends around that vertex. This is the most memory efficient and fastest
primitive to use in all use-cases.  
  
**NOTE** : A circle forms a closed shape and does have an interior therefore
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
      
            // Add a Circle.
            var shapeIndex = shapeGroup.AddCircle
                (
                    center: new [Vector2](Vector2.html)(-2f, 3f),
                    radius: 1f
                );  
      
            // Fetch the actual shape created.
            var physicsShape = shapeGroup.GetShape(shapeIndex);  
      
            // Validate what we created.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), physicsShape.shapeType);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(1f, physicsShape.radius);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1, physicsShape.vertexCount);
        }  
      
        // Get a physics shape from a [Collider](Collider.html).
        void GetShapeFromCollider()
        {
            // Fetch the collider.
            var collider = GetComponent<[CircleCollider2D](CircleCollider2D.html)>();  
      
            // If the collider is not active and enabled then we'll get no shapes.
            // Let's just quit if not.
            if (!collider.isActiveAndEnabled)
                return;  
      
            // Configure the collider.
            collider.radius = 1f;  
      
            // Create a shape group.
            var shapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Get the collider shapes.
            collider.GetShapes(shapeGroup);  
      
            // Fetch the actual shape.
            var physicsShape = shapeGroup.GetShape(0);  
      
            // Validate what we retrieved.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), physicsShape.shapeType);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(1f, physicsShape.radius);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1, physicsShape.vertexCount);
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

