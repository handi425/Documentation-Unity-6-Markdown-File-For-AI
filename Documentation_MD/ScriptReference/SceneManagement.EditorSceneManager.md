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

# EditorSceneManager

class in UnityEditor.SceneManagement

/

Inherits
from:[SceneManagement.SceneManager](SceneManagement.SceneManager.html)

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

Scene management in the Editor.

### Static Properties

[DefaultSceneCullingMask](SceneManagement.EditorSceneManager.DefaultSceneCullingMask.html)|
Use SceneCullingMasks.DefaultSceneCullingMask instead.  
---|---  
[playModeStartScene](SceneManagement.EditorSceneManager-
playModeStartScene.html)| Loads this SceneAsset when you start Play Mode.  
[preventCrossSceneReferences](SceneManagement.EditorSceneManager-
preventCrossSceneReferences.html)| Controls whether cross-Scene references are
allowed in the Editor.  
[previewSceneCount](SceneManagement.EditorSceneManager-
previewSceneCount.html)| The current amount of active preview Scenes.  
  
### Static Methods

[CalculateAvailableSceneCullingMask](SceneManagement.EditorSceneManager.CalculateAvailableSceneCullingMask.html)|
Go through all Scenes and find the smallest unused bit in the unition of all
Scene culling masks.  
---|---  
[ClosePreviewScene](SceneManagement.EditorSceneManager.ClosePreviewScene.html)|
Closes a preview Scene created by NewPreviewScene or OpenPreviewScene.  
[CloseScene](SceneManagement.EditorSceneManager.CloseScene.html)| Close the
Scene. If removeScene flag is true, the closed Scene will also be removed from
EditorSceneManager.  
[DetectCrossSceneReferences](SceneManagement.EditorSceneManager.DetectCrossSceneReferences.html)|
Detects cross-Scene references in a Scene.  
[EnsureUntitledSceneHasBeenSaved](SceneManagement.EditorSceneManager.EnsureUntitledSceneHasBeenSaved.html)|
Shows a save dialog if an Untitled Scene exists in the current Scene manager
setup.  
[GetSceneCullingMask](SceneManagement.EditorSceneManager.GetSceneCullingMask.html)|
Return the culling mask set on the given Scene.  
[GetSceneManagerSetup](SceneManagement.EditorSceneManager.GetSceneManagerSetup.html)|
Returns the current setup of the SceneManager.  
[IsPreviewScene](SceneManagement.EditorSceneManager.IsPreviewScene.html)| Is
the Scene a preview Scene?  
[IsPreviewSceneObject](SceneManagement.EditorSceneManager.IsPreviewSceneObject.html)|
Is this object part of a preview Scene?  
[LoadSceneAsyncInPlayMode](SceneManagement.EditorSceneManager.LoadSceneAsyncInPlayMode.html)|
This method allows you to load a Scene during playmode in the editor, without
requiring the Scene to be included in the Build Settings Scene list.  
[LoadSceneInPlayMode](SceneManagement.EditorSceneManager.LoadSceneInPlayMode.html)|
This method allows you to load a Scene during playmode in the editor, without
requiring the Scene to be included in the Build Settings Scene list.  
[MarkAllScenesDirty](SceneManagement.EditorSceneManager.MarkAllScenesDirty.html)|
Mark all the loaded Scenes as modified.  
[MarkSceneDirty](SceneManagement.EditorSceneManager.MarkSceneDirty.html)| Mark
the specified Scene as modified.  
[MoveSceneAfter](SceneManagement.EditorSceneManager.MoveSceneAfter.html)|
Allows you to reorder the Scenes currently open in the Hierarchy window. Moves
the source Scene so it comes after the destination Scene.  
[MoveSceneBefore](SceneManagement.EditorSceneManager.MoveSceneBefore.html)|
Allows you to reorder the Scenes currently open in the Hierarchy window. Moves
the source Scene so it comes before the destination Scene.  
[NewPreviewScene](SceneManagement.EditorSceneManager.NewPreviewScene.html)|
Creates a new preview Scene. Any object added to a preview Scene will only be
rendered in that Scene.  
[NewScene](SceneManagement.EditorSceneManager.NewScene.html)| Create a new
Scene.  
[OpenPreviewScene](SceneManagement.EditorSceneManager.OpenPreviewScene.html)|
Opens a Scene Asset in a preview Scene.  
[OpenScene](SceneManagement.EditorSceneManager.OpenScene.html)| Open a Scene
in the Editor.  
[RestoreSceneManagerSetup](SceneManagement.EditorSceneManager.RestoreSceneManagerSetup.html)|
Restore the setup of the SceneManager.  
[SaveCurrentModifiedScenesIfUserWantsTo](SceneManagement.EditorSceneManager.SaveCurrentModifiedScenesIfUserWantsTo.html)|
Asks the user if they want to save the current open modified Scene or Scenes
in the Hierarchy.  
[SaveModifiedScenesIfUserWantsTo](SceneManagement.EditorSceneManager.SaveModifiedScenesIfUserWantsTo.html)|
Asks whether the modfied input Scenes should be saved.  
[SaveOpenScenes](SceneManagement.EditorSceneManager.SaveOpenScenes.html)| Save
all open Scenes.  
[SaveScene](SceneManagement.EditorSceneManager.SaveScene.html)| Save a Scene.  
[SaveScenes](SceneManagement.EditorSceneManager.SaveScenes.html)| Save a list
of Scenes.  
[SetSceneCullingMask](SceneManagement.EditorSceneManager.SetSceneCullingMask.html)|
Set the culling mask on this scene to this value. Cameras will only render
objects in Scenes that have the same bits set in their culling mask.  
  
### Events

[activeSceneChangedInEditMode](SceneManagement.EditorSceneManager-
activeSceneChangedInEditMode.html)| Subscribe to this event to get notified
when the active Scene has changed in Edit mode in the Editor.  
---|---  
[newSceneCreated](SceneManagement.EditorSceneManager-newSceneCreated.html)|
This event is called after a new Scene has been created.  
[sceneClosed](SceneManagement.EditorSceneManager-sceneClosed.html)| This event
is called after a Scene has been closed in the editor.  
[sceneClosing](SceneManagement.EditorSceneManager-sceneClosing.html)| This
event is called before closing an open Scene after you have requested that the
Scene is closed.  
[sceneDirtied](SceneManagement.EditorSceneManager-sceneDirtied.html)| This
event is called after a Scene has been modified in the editor.  
[sceneManagerSetupRestored](SceneManagement.EditorSceneManager-
sceneManagerSetupRestored.html)| This can be useful to get notified when the
SceneManager's scenes are replaced with a set of new scenes from calls to
RestoreSceneManagerSetup.Use the scenes argument to check what scenes has just
been opened.Additional resources: SceneManagerSetupRestoredCallback.  
[sceneOpened](SceneManagement.EditorSceneManager-sceneOpened.html)| This event
is called after a Scene has been opened in the editor.  
[sceneOpening](SceneManagement.EditorSceneManager-sceneOpening.html)| This
event is called before opening an existing Scene.  
[sceneSaved](SceneManagement.EditorSceneManager-sceneSaved.html)| This event
is called after a Scene has been saved.  
[sceneSaving](SceneManagement.EditorSceneManager-sceneSaving.html)| This event
is called before a Scene is saved disk after you have requested the Scene to
be saved.  
  
### Delegates

[NewSceneCreatedCallback](SceneManagement.EditorSceneManager.NewSceneCreatedCallback.html)|
Callbacks of this type which have been added to the newSceneCreated event are
called after a new Scene has been created.  
---|---  
[SceneClosedCallback](SceneManagement.EditorSceneManager.SceneClosedCallback.html)|
Callbacks of this type which have been added to the sceneClosed event are
called immediately after the Scene has been closed.  
[SceneClosingCallback](SceneManagement.EditorSceneManager.SceneClosingCallback.html)|
Callbacks of this type which have been added to the sceneClosing event are
called just before a Scene is closed.  
[SceneDirtiedCallback](SceneManagement.EditorSceneManager.SceneDirtiedCallback.html)|
Callbacks of this type which have been added to the sceneDirtied event are
called after a Scene changes from being unmodified to being modified.  
[SceneManagerSetupRestoredCallback](SceneManagement.EditorSceneManager.SceneManagerSetupRestoredCallback.html)|
Callbacks of this type which have been added to the sceneManagerSetupRestored
event are called after RestoreSceneManagerSetup has been called.  
[SceneOpenedCallback](SceneManagement.EditorSceneManager.SceneOpenedCallback.html)|
Callbacks of this type which have been added to the sceneOpened event are
called after a Scene has been opened.  
[SceneOpeningCallback](SceneManagement.EditorSceneManager.SceneOpeningCallback.html)|
Callbacks of this type which have been added to the sceneOpening event are
called just before opening a Scene.  
[SceneSavedCallback](SceneManagement.EditorSceneManager.SceneSavedCallback.html)|
Callbacks of this type which have been added to the sceneSaved event are
called after a Scene has been saved.  
[SceneSavingCallback](SceneManagement.EditorSceneManager.SceneSavingCallback.html)|
Callbacks of this type which have been added to the sceneSaving event are
called just before the Scene is saved.  
  
### Inherited Members

### Static Properties

[loadedSceneCount](SceneManagement.SceneManager-loadedSceneCount.html)| The
number of loaded Scenes.  
---|---  
[sceneCount](SceneManagement.SceneManager-sceneCount.html)| The current number
of Scenes.  
[sceneCountInBuildSettings](SceneManagement.SceneManager-
sceneCountInBuildSettings.html)| Number of Scenes in Build Settings.  
  
### Static Methods

[CreateScene](SceneManagement.SceneManager.CreateScene.html)| Create an empty
new Scene at runtime with the given name.  
---|---  
[GetActiveScene](SceneManagement.SceneManager.GetActiveScene.html)| Gets the
currently active Scene.  
[GetSceneAt](SceneManagement.SceneManager.GetSceneAt.html)| Get the Scene at
index in the SceneManager's list of loaded Scenes.  
[GetSceneByBuildIndex](SceneManagement.SceneManager.GetSceneByBuildIndex.html)|
Get a Scene struct from a build index.  
[GetSceneByName](SceneManagement.SceneManager.GetSceneByName.html)| Searches
through the Scenes loaded for a Scene with the given name.  
[GetSceneByPath](SceneManagement.SceneManager.GetSceneByPath.html)| Searches
all Scenes loaded for a Scene that has the given asset path.  
[LoadScene](SceneManagement.SceneManager.LoadScene.html)| Loads the Scene by
its name or index in Build Settings.  
[LoadSceneAsync](SceneManagement.SceneManager.LoadSceneAsync.html)| Loads the
Scene asynchronously in the background.  
[MergeScenes](SceneManagement.SceneManager.MergeScenes.html)| This will merge
the source Scene into the destinationScene.  
[MoveGameObjectsToScene](SceneManagement.SceneManager.MoveGameObjectsToScene.html)|
Move multiple GameObjects, represented by a NativeArray of instance IDs, from
their current Scene to a new Scene.  
[MoveGameObjectToScene](SceneManagement.SceneManager.MoveGameObjectToScene.html)|
Move a GameObject from its current Scene to a new Scene.  
[SetActiveScene](SceneManagement.SceneManager.SetActiveScene.html)| Set the
Scene to be active.  
[UnloadSceneAsync](SceneManagement.SceneManager.UnloadSceneAsync.html)|
Destroys all GameObjects associated with the given Scene and removes the Scene
from the SceneManager.  
  
### Events

[activeSceneChanged](SceneManagement.SceneManager-activeSceneChanged.html)|
Subscribe to this event to get notified when the active Scene has changed.  
---|---  
[sceneLoaded](SceneManagement.SceneManager-sceneLoaded.html)| Assign a custom
callback to this event to get notifications when a Scene has loaded.  
[sceneUnloaded](SceneManagement.SceneManager-sceneUnloaded.html)| Add a
delegate to this to get notifications when a Scene has unloaded.  
  
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

