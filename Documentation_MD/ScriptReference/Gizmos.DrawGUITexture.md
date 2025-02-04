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

#  [Gizmos](Gizmos.html).DrawGUITexture

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

public static void DrawGUITexture([Rect](Rect.html) screenRect,
[Texture](Texture.html) texture, [Material](Material.html) mat = null);

## Declaration

public static void DrawGUITexture([Rect](Rect.html) screenRect,
[Texture](Texture.html) texture, int leftBorder, int rightBorder, int
topBorder, int bottomBorder, [Material](Material.html) mat = null);

### Parameters

screenRect | The size and position of the texture on the "screen" defined by the XY plane.  
---|---  
texture | The texture to be displayed.  
mat | An optional material to apply the texture.  
leftBorder | Inset from the rectangle's left edge.  
rightBorder | Inset from the rectangle's right edge.  
topBorder | Inset from the rectangle's top edge.  
bottomBorder | Inset from the rectangle's bottom edge.  
  
### Description

Draw a texture in the Scene.

The chosen texture is drawn in 3D space on a "screen" defined by the XY plane
(ie, the plane where the Z coordinate is zero). The values of the texture
rectangle are given in Scene units. The optional border values specify an
inset from each edge within the rectangle in Scene units; the texture is drawn
inside the inset rectangle and the edge pixels are repeated outwards. This is
a useful quick way to create a large background region around the main texture
when its edges are of a single colour.  
  
This function can be useful for creating GUI backgrounds in conjunction with a
camera pointing directly at the texture.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture](Texture.html) myTexture;  
      
        void OnDrawGizmosSelected()
        {
            // Draw a texture rectangle on the XY plane of the scene
            [Gizmos.DrawGUITexture](Gizmos.DrawGUITexture.html)(new [Rect](Rect.html)(10, 10, 20, 20), myTexture);
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

