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

#  [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).vertexCount

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

public int vertexCount;

### Description

The total number of vertices in the shape group used to represent all
[PhysicsShape2D](PhysicsShape2D.html) within it. (Read Only)

    
    
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        private const int ShapeCount = 10;  
      
        void Start()
        {
            // Create a shape group.
            // NOTE: We can hint to the shape group the capacity for shapes so that it's quicker when adding them.
            var shapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)(shapeCapacity: ShapeCount);  
      
            // Add Boxes to the shape group.
            for (var n = 0; n < ShapeCount; ++n)
            {
                shapeGroup.AddBox
                    (
                        center: new [Vector2](Vector2.html)(n, 0f),
                        size: new [Vector2](Vector2.html)(0.25f, 0.25f)
                    );
            }  
      
            // Validate that we created the specified number of shapes.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(ShapeCount, shapeGroup.shapeCount);  
      
            // Validate that we created the correct number of vertices.
            // NOTE: Each [Box](UIElements.Box.html) has 4 vertices so we multiply this constant by the number of shapes.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(ShapeCount * 4, shapeGroup.vertexCount);  
      
            // Validate each shape.
            for (var n = 0; n < ShapeCount; ++n)
            {
                // Fetch the actual shape created.
                var physicsShape = shapeGroup.GetShape(n);  
      
                // Validate the shape.
                [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Polygon](PhysicsShapeType2D.Polygon.html), physicsShape.shapeType);
                [Assert.AreEqual](Assertions.Assert.AreEqual.html)(4, physicsShape.vertexCount);
            }
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

