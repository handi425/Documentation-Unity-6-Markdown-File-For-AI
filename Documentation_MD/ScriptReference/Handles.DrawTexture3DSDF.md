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

#  [Handles](Handles.html).DrawTexture3DSDF

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

public static void DrawTexture3DSDF([Texture](Texture.html) texture, float
stepScale = 1.0f, float surfaceOffset = 0.0f, [Gradient](Gradient.html)
customColorRamp = null);

### Parameters

texture | The volumetric texture to draw.  
---|---  
stepScale | The number by which to multiply the ray step size. The ray step size is the distance between 2 neighboring pixels. The default value is 1.  
surfaceOffset | The intensity of the pixels at which the surface is rendered. When this value is positive, Unity will expand the rendered surface. When this value is negative, Unity will render empty space as a surface, and a surface as empty space. The default value is 0.  
customColorRamp | The custom gradient that Unity uses as a color ramp. If this is not specified, Unity uses [Google Turbo color ramp](https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html).  
  
### Description

Draws a 3D texture using Signed Distance Field rendering mode in 3D space.

This visualization mode supports only non-directional Signed Distance Fields.  
  
![](../StaticFiles/ScriptRefImages/3DTextureHandleCorridorSDF.png)  
_Corridor SDF visualized using Google Turbo color ramp._

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    [[ExecuteInEditMode](ExecuteInEditMode.html)]
    public class Reference : [MonoBehaviour](MonoBehaviour.html)
    {
        public [Texture3D](Texture3D.html) texture;
        public float stepScale = 1;
        public float surfaceOffset;
        public bool useCustomColorRamp;  
      
        // We should initialize this gradient before using it as a custom color ramp
        public [Gradient](Gradient.html) customColorRampGradient;
    }  
      
    [[CanEditMultipleObjects](CanEditMultipleObjects.html)]
    [[CustomEditor](CustomEditor.html)(typeof(Reference))]
    public class Handle : [Editor](Editor.html)
    {
        private void OnSceneViewGUI([SceneView](SceneView.html) sv)
        {
            Object[] objects = targets;
            foreach (var obj in objects)
            {
                Reference reference = obj as Reference;
                if (reference != null && reference.texture != null)
                {
                    [Handles.matrix](Handles-matrix.html) = reference.transform.localToWorldMatrix;
                    [Handles.DrawTexture3DSDF](Handles.DrawTexture3DSDF.html)(reference.texture, reference.stepScale, reference.surfaceOffset,
                        reference.useCustomColorRamp ? reference.customColorRampGradient : null);
                }
            }
        }  
      
        void OnEnable()
        {
            [SceneView.duringSceneGui](SceneView-duringSceneGui.html) += OnSceneViewGUI;
        }  
      
        void OnDisable()
        {
            [SceneView.duringSceneGui](SceneView-duringSceneGui.html) -= OnSceneViewGUI;
        }
    }
    

Additional resources:
[Handles.DrawTexture3DSlice](Handles.DrawTexture3DSlice.html),
[Handles.DrawTexture3DVolume](Handles.DrawTexture3DVolume.html),
[Texture3D](Texture3D.html), [Gradient](Gradient.html).

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

