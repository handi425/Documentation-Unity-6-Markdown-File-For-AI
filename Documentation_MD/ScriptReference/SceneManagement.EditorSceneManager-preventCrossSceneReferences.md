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
[EditorSceneManager](SceneManagement.EditorSceneManager.html).preventCrossSceneReferences

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

public static bool preventCrossSceneReferences;

### Description

Controls whether cross-Scene references are allowed in the Editor.

A cross-Scene reference occurs when you have multiple Scenes loaded in the
Editor, and a component attached to a GameObject in one Scene has a reference
to a GameObject in another Scene.  
  
The default value for this setting is 'true'. This means that by default, you
cannot create cross-Scene references in the Unity Editor.  
  
This is prevented by default because cross-Scene references cannot be saved in
Scene files. Therefore, having the Editor prevent you from creating these
references avoids potential situations where your assignments cannot be saved.
If you need cross-Scene references at runtime, you need to create those
references at runtime - finding the GameObjects by values such as name or tag.  
  
There are, however, certain situations where you may need to create cross-
Scene references in the Editor, even though these references cannot be saved -
for example, if you needed to create an Editor script which should be able to
operate on GameObjects from many Scenes at once. Deactivating this setting
allows you to do this.  
  
Note however that deactivating this value does not mean cross-Scene references
will be saved.  
  
Disabling this setting means that:  
  
1) Dragging references from a GameObject in one Scene to another GameObject's
Component field in a different Scene is allowed.  
2) The Object Picker (the small target icon next to most assignable fields in
the Inspector) lists choices from all open Scenes, instead of just the
GameObject's own Scene.  
3) Dragging GameObjects from one Scene to another Scene can result in cross-
Scene references. Warnings are no longer logged when this happens.  

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

