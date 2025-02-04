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
[TerrainPaintTool<T0>](TerrainTools.TerrainPaintTool_1.html).OnRenderBrushPreview

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

public void OnRenderBrushPreview([Terrain](Terrain.html) terrain,
[TerrainTools.IOnSceneGUI](TerrainTools.IOnSceneGUI.html) editContext);

### Parameters

terrain | Active Terrain object.  
---|---  
editContext | Interface for communication between Editor and Paint tools.  
  
### Description

Use this method to implement custom tool preview and UI behavior that will
only render while the mouse is within the [SceneView](SceneView.html) bounds
or while you're actively using this tool.

Unity calls this method when the mouse is within the
[SceneView](SceneView.html) viewport bounds, and the
EditorGUIUtility.hotControl is set to 0 or to the [Terrain](Terrain.html)
control ID provided by the [IOnSceneGUI](TerrainTools.IOnSceneGUI.html)
context instance. This is usually when no other tools are active, or when
you're actively using this tool.  
  
Additional resources: [Editor.OnSceneGUI](Editor.OnSceneGUI.html),
[SceneView](SceneView.html), TerrainPaintTool_1.OnSceneGUI,
EditorGUIUtility.hotControl, [GUIUtility.hotControl](GUIUtility-
hotControl.html).

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

