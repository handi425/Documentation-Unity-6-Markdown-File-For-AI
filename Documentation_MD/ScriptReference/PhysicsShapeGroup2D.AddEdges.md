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

#  [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).AddEdges

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

public int AddEdges(List<Vector2> vertices, float edgeRadius = 0f);

### Parameters

vertices | A list of vertices that represent a continuous set of edges with each vertex connecting to the following vertex to form each edge.  
---|---  
edgeRadius | The radius extending around each edge. This is identical to [EdgeCollider2D.edgeRadius](EdgeCollider2D-edgeRadius.html).  
  
### Returns

**int** Returns the shape index the shape was added to in the
[PhysicsShapeGroup2D](PhysicsShapeGroup2D.html). This index is used as the
main reference when retrieving a shape.

### Description

Adds an edges shape
([PhysicsShapeType2D.Edges](PhysicsShapeType2D.Edges.html)) to the shape
group.

An edge shape is comprised of multiple edges (line segments) defined by all
the specified `vertices` and an `edgeRadius` that extends around the all the
edge(s).  
  
**NOTE** : Edges do not form closed a shape as they do not have any interior
even if the first and last vertex were to overlap therefore the logical
interior is not detectable by physics queries etc.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
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
      
            // Add a list of Edges.
            var shapeIndex = shapeGroup.AddEdges
                (
                    vertices: new List<[Vector2](Vector2.html)>
                    {
                        new [Vector2](Vector2.html)(-4f, 0f),
                        new [Vector2](Vector2.html)(-2f, -0.5f),
                        new [Vector2](Vector2.html)(0f, 0f),
                        new [Vector2](Vector2.html)(2f, -0.5f),
                        new [Vector2](Vector2.html)(4f, 0f),
                    },
                    edgeRadius: 0.5f
                );  
      
            // Fetch the actual shape created.
            var physicsShape = shapeGroup.GetShape(shapeIndex);  
      
            // Validate what we created.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Edges](PhysicsShapeType2D.Edges.html), physicsShape.shapeType);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.5f, physicsShape.radius);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(5, physicsShape.vertexCount);
        }  
      
        // Get a physics shape from a [Collider](Collider.html).
        void GetShapeFromCollider()
        {
            // Fetch the collider.
            var collider = GetComponent<[EdgeCollider2D](EdgeCollider2D.html)>();  
      
            // If the collider is not active and enabled then we'll get no shapes.
            // Let's just quit if not.
            if (!collider.isActiveAndEnabled)
                return;  
      
            // Configure the collider.
            collider.SetPoints(
                new List<[Vector2](Vector2.html)>()
                {
                    new [Vector2](Vector2.html)(-4f, 0f),
                    new [Vector2](Vector2.html)(-2f, -0.5f),
                    new [Vector2](Vector2.html)(0f, 0f),
                    new [Vector2](Vector2.html)(2f, -0.5f),
                    new [Vector2](Vector2.html)(4f, 0f),
                });
            collider.edgeRadius = 0.5f;  
      
            // Create a shape group.
            var shapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Get the collider shapes.
            collider.GetShapes(shapeGroup);  
      
            // Fetch the actual shape.
            var physicsShape = shapeGroup.GetShape(0);  
      
            // Validate what we retrieved.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Edges](PhysicsShapeType2D.Edges.html), physicsShape.shapeType);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.5f, physicsShape.radius);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(5, physicsShape.vertexCount);
        }
    }
    

* * *

## Declaration

public int AddEdges(List<Vector2> vertices, bool useAdjacentStart, bool
useAdjacentEnd, [Vector2](Vector2.html) adjacentStart, [Vector2](Vector2.html)
adjacentEnd, float edgeRadius = 0f);

### Parameters

vertices | A list of vertices that represent a continuous set of edges with each vertex connecting to the following vertex to form each edge.  
---|---  
edgeRadius | The radius extending around each edge. This is identical to [EdgeCollider2D.edgeRadius](EdgeCollider2D-edgeRadius.html).  
useAdjacentStart | When the value is true, the `adjacentStart` argument is used. When the value is false, the `adjacentStart` argument is not used.  
useAdjacentEnd | When the value is true, the `adjacentEnd` argument is used. When the value is false, the `adjacentEnd` argument is not used.  
adjacentStart | Defines the position of a virtual point adjacent to the start vertex of an edge shape.  
adjacentEnd | Defines the position of a virtual point adjacent to the end vertex of an edge shape.  
  
### Returns

**int** Returns the shape index the shape was added to in the
[PhysicsShapeGroup2D](PhysicsShapeGroup2D.html). This index is used as the
main reference when retrieving a shape.

### Description

Adds an edge shape ([PhysicsShapeType2D.Edges](PhysicsShapeType2D.Edges.html))
to the shape group supporting adjacent start and end vertices.

An edges shape is comprised of multiple edges (line segments) defined by all
the specified `vertices` and an `edgeRadius` that extends around the all the
edge(s).  
  
**NOTE** : Edges do not form closed a shape as they do not have any interior
even if the first and last vertex were to overlap therefore the logical
interior is not detectable by physics queries etc.

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

