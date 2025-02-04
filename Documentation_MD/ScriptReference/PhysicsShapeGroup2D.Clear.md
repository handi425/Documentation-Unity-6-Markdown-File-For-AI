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

#  [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).Clear

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

public void Clear();

### Description

Clears all the vertices and shapes from the PhysicsShapeGroup.

This call clears the lists used to store both vertices and shapes but retains
the current shape group capacity (effectively creating an empty shape group).

    
    
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Create a shape group.
            var shapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Add a Circle to the shape group.
            shapeGroup.AddCircle
                (
                    center: [Vector2.zero](Vector2-zero.html),
                    radius: 1f
                );  
      
            // Add a [Box](UIElements.Box.html) to the shape group.
            shapeGroup.AddBox
                (
                    center: new [Vector2](Vector2.html)(3f, 2f),
                    size: new [Vector2](Vector2.html)(1f, 1f)
                );  
      
            // Validate the contents.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1 + 1, shapeGroup.shapeCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1 + 4, shapeGroup.vertexCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), shapeGroup.GetShape(0).shapeType);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Polygon](PhysicsShapeType2D.Polygon.html), shapeGroup.GetShape(1).shapeType);  
      
            // Clear the shape group.
            shapeGroup.Clear();  
      
            // Validate the contents.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(0, shapeGroup.shapeCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(0, shapeGroup.vertexCount);
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

