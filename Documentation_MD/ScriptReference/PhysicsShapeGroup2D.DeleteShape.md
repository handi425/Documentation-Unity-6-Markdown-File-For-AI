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

#  [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).DeleteShape

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

public void DeleteShape(int shapeIndex);

### Parameters

shapeIndex | The index of the shape stored the [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).  
---|---  
  
### Description

When destroying a shape at the specified `shapeIndex`, all other shapes that
exist above the specified `shapeIndex` will have their shape indices updated
appropriately.

    
    
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Create a shape group.
            var shapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Add two Circles to the shape group.
            shapeGroup.AddCircle
                (
                    center: [Vector2.left](Vector2-left.html),
                    radius: 1f
                );
            var shapeIndex = shapeGroup.AddCircle
                (
                    center: [Vector2.right](Vector2-right.html),
                    radius: 1f
                );  
      
            // Add a [Box](UIElements.Box.html) to the shape group.
            shapeGroup.AddBox
                (
                    center: new [Vector2](Vector2.html)(3f, 2f),
                    size: new [Vector2](Vector2.html)(1f, 1f)
                );  
      
            // Validate the contents.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1 + 1 + 1, shapeGroup.shapeCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1 + 1 + 4, shapeGroup.vertexCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), shapeGroup.GetShape(0).shapeType);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), shapeGroup.GetShape(1).shapeType);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Polygon](PhysicsShapeType2D.Polygon.html), shapeGroup.GetShape(2).shapeType);  
      
            // Delete the second Circle shape.
            shapeGroup.DeleteShape(shapeIndex);  
      
            // Validate the contents.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1 + 1, shapeGroup.shapeCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1 + 4, shapeGroup.vertexCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), shapeGroup.GetShape(0).shapeType);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Polygon](PhysicsShapeType2D.Polygon.html), shapeGroup.GetShape(1).shapeType);
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

