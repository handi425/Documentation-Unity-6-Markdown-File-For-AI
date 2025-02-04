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

#  [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).SetShapeVertex

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

public void SetShapeVertex(int shapeIndex, int vertexIndex,
[Vector2](Vector2.html) vertex);

### Parameters

shapeIndex | The index of the shape stored in the [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html). The shape index is zero-based with the shape group having a quantity of shapes specified by [shapeCount](PhysicsShapeGroup2D-shapeCount.html).  
---|---  
vertexIndex | The index of the shape vertex stored in the [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html). The vertex index is zero-based with the shape having a quantity of vertex specified by [PhysicsShape2D.vertexCount](PhysicsShape2D-vertexCount.html).  
vertex | The value to set the shape vertex to.  
  
### Description

Sets a single vertex of a shape.

**NOTE** : When accessing multiple vertices, it is more efficient to do one of
the following:

  * Get all the shape vertices using [GetShapeVertices](PhysicsShapeGroup2D.GetShapeVertices.html)
  * Get all the shape group vertices using [GetShapeData](PhysicsShapeGroup2D.GetShapeData.html)
  * Create the [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html) with explicit shapes and vertices lists using the shape group [Constructor](PhysicsShapeGroup2D-ctor.html)

Additional resources:
[GetShapeVertex](PhysicsShapeGroup2D.GetShapeVertex.html).

    
    
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Create a shape group.
            var shapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Add a Capsule to the shape group.
            var shapeIndex = shapeGroup.AddCapsule
                (
                    vertex0: [Vector2.down](Vector2-down.html),
                    vertex1: [Vector2.up](Vector2-up.html),
                    radius: 0.5f
                );  
      
            // Fetch the shape vertices from the shape group.
            var vertex0 = shapeGroup.GetShapeVertex(shapeIndex, vertexIndex: 0);
            var vertex1 = shapeGroup.GetShapeVertex(shapeIndex, vertexIndex: 1);  
      
            // Validate the Capsule vertices.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([Vector2.down](Vector2-down.html), vertex0);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([Vector2.up](Vector2-up.html), vertex1);  
      
            // Set the shape vertices in the shape group.
            shapeGroup.SetShapeVertex(shapeIndex, vertexIndex: 0, vertex: [Vector2.left](Vector2-left.html));
            shapeGroup.SetShapeVertex(shapeIndex, vertexIndex: 1, vertex: [Vector2.right](Vector2-right.html));  
      
            // Fetch the shape vertices from the shape group.
            vertex0 = shapeGroup.GetShapeVertex(shapeIndex, vertexIndex: 0);
            vertex1 = shapeGroup.GetShapeVertex(shapeIndex, vertexIndex: 1);  
      
            // Validate the Capsule vertices.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([Vector2.left](Vector2-left.html), vertex0);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([Vector2.right](Vector2-right.html), vertex1);
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

