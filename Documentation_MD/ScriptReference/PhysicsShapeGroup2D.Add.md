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

#  [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).Add

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

public void Add([PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)
physicsShapeGroup);

### Parameters

physicsShapeGroup | The [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html) to add to this shape group. (Read Only)  
---|---  
  
### Description

Adds a copy of all the [PhysicsShape2D](PhysicsShape2D.html) and their
geometry from the specified `physicsShapeGroup` into this shape group. The
specified `physicsShapeGroup` is not modified.

    
    
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        private const int ShapeCount = 10;  
      
        void Start()
        {
            // Create a shape group and add a Circle to it.
            var shapeGroup1 = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();
            shapeGroup1.AddCircle
                (
                    center: [Vector2.zero](Vector2-zero.html),
                    radius: 1f
                );  
      
            // Validate the contents.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1, shapeGroup1.shapeCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1, shapeGroup1.vertexCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), shapeGroup1.GetShape(0).shapeType);  
      
            // Create another shape group and add a [Box](UIElements.Box.html) to it.
            var shapeGroup2 = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();
            shapeGroup2.AddBox
                (
                    center: new [Vector2](Vector2.html)(3f, 2f),
                    size: new [Vector2](Vector2.html)(1f, 1f)
                );  
      
            // Validate the contents.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1, shapeGroup2.shapeCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(4, shapeGroup2.vertexCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Polygon](PhysicsShapeType2D.Polygon.html), shapeGroup2.GetShape(0).shapeType);  
      
            // Add the second shape group to the first shape group.
            shapeGroup1.Add(shapeGroup2);  
      
            // Validate the contents.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1 + 1, shapeGroup1.shapeCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1 + 4, shapeGroup1.vertexCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), shapeGroup1.GetShape(0).shapeType);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Polygon](PhysicsShapeType2D.Polygon.html), shapeGroup1.GetShape(1).shapeType);
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

