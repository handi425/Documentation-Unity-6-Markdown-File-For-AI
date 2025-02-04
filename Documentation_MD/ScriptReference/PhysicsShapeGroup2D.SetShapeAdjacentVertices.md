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

#  [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).SetShapeAdjacentVertices

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

public void SetShapeAdjacentVertices(int shapeIndex, bool useAdjacentStart,
bool useAdjacentEnd, [Vector2](Vector2.html) adjacentStart,
[Vector2](Vector2.html) adjacentEnd);

### Parameters

shapeIndex | The index of the shape to be modified that is stored the [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).  
---|---  
useAdjacentStart | Sets the [PhysicsShape2D.useAdjacentStart](PhysicsShape2D-useAdjacentStart.html) property of the selected shape.  
useAdjacentEnd | Sets the [PhysicsShape2D.useAdjacentEnd](PhysicsShape2D-useAdjacentEnd.html) property of the selected shape.  
adjacentStart | Sets the [PhysicsShape2D.adjacentStart](PhysicsShape2D-adjacentStart.html) property of the selected shape.  
adjacentEnd | Sets the [PhysicsShape2D.adjacentEnd](PhysicsShape2D-adjacentEnd.html) property of the selected shape.  
  
### Description

Sets the adjacent vertices of a shape.

**NOTE** : Calling this on a [PhysicsShape2D](PhysicsShape2D.html) that does
not have a [shapeType](PhysicsShape2D-shapeType.html) of
[PhysicsShapeType2D.Edges](PhysicsShapeType2D.Edges.html) will result in an
exception being thrown.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
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
      
                    edgeRadius: 0.5f,  
      
                    useAdjacentStart: true,
                    useAdjacentEnd: true,
                    adjacentStart: new [Vector2](Vector2.html)(-5f, -1f),
                    adjacentEnd: new [Vector2](Vector2.html)(6f, 2f)
                );  
      
            // Fetch the actual shape created.
            var physicsShape = shapeGroup.GetShape(shapeIndex);  
      
            // Validate what we created.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Edges](PhysicsShapeType2D.Edges.html), physicsShape.shapeType);
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(0.5f, physicsShape.radius);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(5, physicsShape.vertexCount);
            [Assert.IsTrue](Assertions.Assert.IsTrue.html)(physicsShape.useAdjacentStart);
            [Assert.IsTrue](Assertions.Assert.IsTrue.html)(physicsShape.useAdjacentEnd);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(new [Vector2](Vector2.html)(-5f, -1f), physicsShape.adjacentStart);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(new [Vector2](Vector2.html)(6f, 2f), physicsShape.adjacentEnd);  
      
            // Set the adjacent vertices.
            shapeGroup.SetShapeAdjacentVertices(
                shapeIndex,
                useAdjacentStart: true,
                useAdjacentEnd: true,
                adjacentStart: new [Vector2](Vector2.html)(-10f, -5f),
                adjacentEnd: new [Vector2](Vector2.html)(12f, 3f));  
      
            // Fetch the updated shape.
            physicsShape = shapeGroup.GetShape(shapeIndex);  
      
            // Validate what we updated.
            [Assert.IsTrue](Assertions.Assert.IsTrue.html)(physicsShape.useAdjacentStart);
            [Assert.IsTrue](Assertions.Assert.IsTrue.html)(physicsShape.useAdjacentEnd);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(new [Vector2](Vector2.html)(-10f, -5f), physicsShape.adjacentStart);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(new [Vector2](Vector2.html)(12f, 3f), physicsShape.adjacentEnd);
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

