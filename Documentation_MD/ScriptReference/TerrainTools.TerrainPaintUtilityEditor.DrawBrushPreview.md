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

#
[TerrainPaintUtilityEditor](TerrainTools.TerrainPaintUtilityEditor.html).DrawBrushPreview(PaintContext,BrushPreview,Texture,BrushTransform,Material,int)

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

### Parameters

heightmapPC | PaintContext describing the heightmap from which to build the preview mesh.  
---|---  
previewTexture | Specifies Whether to build the mesh using the source or destination render texture in heightmapPC.  
brushTexture | The brush texture to preview.  
brushXform | Describes the position and orientation of the brush.  
proceduralMaterial | Material used to render the preview.  
materialPassIndex | Material pass to render.  
  
### Description

Draws a Terrain brush preview mesh from a heightmap PaintContext using the
provided procedural material.

The heightmapPC is used to build the mesh. To ensure that the preview is
rendered on the mesh, the heightmapPC must contain an area around the brush.
To facilitate proper transformation of brush UV space, this method sets up the
brush transforms in the material. Important: The material provided must
support procedural mesh generation in the vertex shader using the shader
functions provided in TerrainPreview.cginc. A default implementation of the
material is provided by GetDefaultBrushPreviewMaterial().  
  
Additional resources:
[TerrainPaintUtilityEditor.GetDefaultBrushPreviewMaterial](TerrainTools.TerrainPaintUtilityEditor.GetDefaultBrushPreviewMaterial.html)
and [PaintContext](TerrainTools.PaintContext.html).

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

