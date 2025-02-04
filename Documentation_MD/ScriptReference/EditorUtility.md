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

# EditorUtility

class in UnityEditor

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

### Description

Editor utility functions.

### Static Properties

[scriptCompilationFailed](EditorUtility-scriptCompilationFailed.html)| True if
there are any compilation error messages in the log.  
---|---  
  
### Static Methods

[ClearDefaultParentObject](EditorUtility.ClearDefaultParentObject.html)|
Clears the default parent GameObject from either a specific Scene or the
active Scene.  
---|---  
[ClearDirty](EditorUtility.ClearDirty.html)| Clear target's dirty flag.  
[ClearProgressBar](EditorUtility.ClearProgressBar.html)| Removes the progress
bar.  
[CollectDeepHierarchy](EditorUtility.CollectDeepHierarchy.html)| Collect all
objects in the hierarchy rooted at each of the given objects.  
[CollectDependencies](EditorUtility.CollectDependencies.html)| Calculates and
returns a list of all assets the assets listed in roots depend on.  
[CompressCubemapTexture](EditorUtility.CompressCubemapTexture.html)| Compress
a cubemap texture.  
[CompressTexture](EditorUtility.CompressTexture.html)| Compress a texture.  
[CopySerialized](EditorUtility.CopySerialized.html)| Copy all settings of a
Unity Object.  
[CopySerializedIfDifferent](EditorUtility.CopySerializedIfDifferent.html)|
Copy all settings of a Unity Object to a second Object if they differ.  
[CopySerializedManagedFieldsOnly](EditorUtility.CopySerializedManagedFieldsOnly.html)|
Copies the serializable fields from one managed object to another.  
[CreateGameObjectWithHideFlags](EditorUtility.CreateGameObjectWithHideFlags.html)|
Creates a game object with HideFlags and specified components.  
[DisplayCancelableProgressBar](EditorUtility.DisplayCancelableProgressBar.html)|
Displays or updates a progress bar that has a cancel button.  
[DisplayDialog](EditorUtility.DisplayDialog.html)| This method displays a
modal dialog.  
[DisplayDialogComplex](EditorUtility.DisplayDialogComplex.html)| Displays a
modal dialog with three buttons.  
[DisplayPopupMenu](EditorUtility.DisplayPopupMenu.html)| Displays a popup
menu.  
[DisplayProgressBar](EditorUtility.DisplayProgressBar.html)| Displays or
updates a progress bar.  
[FocusProjectWindow](EditorUtility.FocusProjectWindow.html)| Brings the
project window to the front and focuses it.  
[FormatBytes](EditorUtility.FormatBytes.html)| Returns a text for a number of
bytes.  
[GetDialogOptOutDecision](EditorUtility.GetDialogOptOutDecision.html)| This
method displays a modal dialog that lets the user opt-out of being shown the
current dialog box again.  
[GetDirtyCount](EditorUtility.GetDirtyCount.html)| Returns an integer that
indicates the number of times the specified object's serialized properties
have changed.  
[GetObjectEnabled](EditorUtility.GetObjectEnabled.html)| Is the object enabled
(0 disabled, 1 enabled, -1 has no enabled button).  
[InstanceIDToObject](EditorUtility.InstanceIDToObject.html)| Translates an
instance ID to a reference to an object.  
[IsDirty](EditorUtility.IsDirty.html)| Gets a boolean value that indicates
whether the specified object has changed since the last time it was saved.  
[IsPersistent](EditorUtility.IsPersistent.html)| Determines if an object is
stored on disk.  
[IsRunningUnderCPUEmulation](EditorUtility.IsRunningUnderCPUEmulation.html)|
Gets a boolean value. This value indicates whether your CPU is unable to
execute Unity natively and is running an emulated version.  
[IsUnityExtensionsInitialized](EditorUtility.IsUnityExtensionsInitialized.html)|
Returns a boolean value which represents the state of initialization of Unity
extensions.  
[IsValidUnityYAML](EditorUtility.IsValidUnityYAML.html)| Returns true if the
provided string can be parsed as YAML.  
[NaturalCompare](EditorUtility.NaturalCompare.html)| Human-like sorting.  
[OpenFilePanel](EditorUtility.OpenFilePanel.html)| Displays the "open file"
dialog and returns the selected path name.  
[OpenFilePanelWithFilters](EditorUtility.OpenFilePanelWithFilters.html)|
Displays the "open file" dialog and returns the selected path name.  
[OpenFolderPanel](EditorUtility.OpenFolderPanel.html)| Displays the "open
folder" dialog and returns the selected path name.  
[OpenPropertyEditor](EditorUtility.OpenPropertyEditor.html)| Open properties
editor for an Object.  
[RequestScriptReload](EditorUtility.RequestScriptReload.html)| The Unity
Editor reloads script assemblies asynchronously on the next frame. This resets
the state of all the scripts, but Unity does not compile any code that has
changed since the previous compilation.  
[SaveFilePanel](EditorUtility.SaveFilePanel.html)| Displays the "save file"
dialog and returns the selected path name.  
[SaveFilePanelInProject](EditorUtility.SaveFilePanelInProject.html)| Displays
the "save file" dialog in the Assets folder of the project and returns the
selected path name.  
[SaveFolderPanel](EditorUtility.SaveFolderPanel.html)| Displays the "save
folder" dialog and returns the selected path name.  
[SetCameraAnimateMaterials](EditorUtility.SetCameraAnimateMaterials.html)|
Sets this camera to allow animation of materials in the Editor.  
[SetCameraAnimateMaterialsTime](EditorUtility.SetCameraAnimateMaterialsTime.html)|
Sets the global time for this camera to use when rendering.  
[SetCustomDiffTool](EditorUtility.SetCustomDiffTool.html)| Set custom diff
tool settings.  
[SetDefaultParentObject](EditorUtility.SetDefaultParentObject.html)| Sets the
default parent object for the active Scene.  
[SetDialogOptOutDecision](EditorUtility.SetDialogOptOutDecision.html)| This
method displays a modal dialog that lets the user opt-out of being shown the
current dialog box again.  
[SetDirty](EditorUtility.SetDirty.html)| Marks target object as dirty.  
[SetObjectEnabled](EditorUtility.SetObjectEnabled.html)| Set the enabled state
of the object.  
[SetSelectedRenderState](EditorUtility.SetSelectedRenderState.html)| Set the
Scene View selected display mode for this Renderer.  
[UnloadUnusedAssetsImmediate](EditorUtility.UnloadUnusedAssetsImmediate.html)|
Unloads assets that are not used.  
[UpdateGlobalShaderProperties](EditorUtility.UpdateGlobalShaderProperties.html)|
Updates the global shader properties to use when rendering.  
  
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

