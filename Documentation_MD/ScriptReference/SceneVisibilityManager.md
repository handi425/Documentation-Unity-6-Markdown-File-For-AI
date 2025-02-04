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

# SceneVisibilityManager

class in UnityEditor

/

Inherits from:[ScriptableSingleton_1](ScriptableSingleton_1.html)

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

Manages Scene Visibility in the editor.

### Public Methods

[AreAllDescendantsHidden](SceneVisibilityManager.AreAllDescendantsHidden.html)|
Checks whether all the descendants of a GameObject are hidden.  
---|---  
[AreAllDescendantsVisible](SceneVisibilityManager.AreAllDescendantsVisible.html)|
Checks whether all the descendants are visible.  
[AreAnyDescendantsHidden](SceneVisibilityManager.AreAnyDescendantsHidden.html)|
Checks whether any descendants are hidden.  
[DisableAllPicking](SceneVisibilityManager.DisableAllPicking.html)| Disables
picking on all GameObjects.  
[DisablePicking](SceneVisibilityManager.DisablePicking.html)| Disables picking
on a GameObject, or an Array of GameObjects, and their descendants.  
[EnableAllPicking](SceneVisibilityManager.EnableAllPicking.html)| Enables
picking on all GameObjects.  
[EnablePicking](SceneVisibilityManager.EnablePicking.html)| Enables picking on
a GameObject, or an array of GameObjects, and its descendants.  
[ExitIsolation](SceneVisibilityManager.ExitIsolation.html)| Exits Isolation
Mode.  
[Hide](SceneVisibilityManager.Hide.html)| Hides a GameObject, or an Array of
GameObjects, and their descendants.  
[HideAll](SceneVisibilityManager.HideAll.html)| Hides all GameObjects.  
[IsCurrentStageIsolated](SceneVisibilityManager.IsCurrentStageIsolated.html)|
Checks whether the current stage is in Isolation mode.  
[IsHidden](SceneVisibilityManager.IsHidden.html)| Checks the hidden state of a
GameObject and, optionally, its descendants.  
[Isolate](SceneVisibilityManager.Isolate.html)| Isolates a GameObject and its
descendants.  
[IsPickingDisabled](SceneVisibilityManager.IsPickingDisabled.html)| Checks the
picking state of a GameObject and, optionally, its descendants.  
[IsPickingDisabledOnAllDescendants](SceneVisibilityManager.IsPickingDisabledOnAllDescendants.html)|
Checks whether all the descendants of a GameObject have picking disabled.  
[IsPickingDisabledOnAnyDescendant](SceneVisibilityManager.IsPickingDisabledOnAnyDescendant.html)|
Checks whether any descendants have picking disabled.  
[IsPickingEnabledOnAllDescendants](SceneVisibilityManager.IsPickingEnabledOnAllDescendants.html)|
Checks whether all the descendants are pickable.  
[Show](SceneVisibilityManager.Show.html)| Shows a GameObject, or an array of
GameObjects, and its descendants.  
[ShowAll](SceneVisibilityManager.ShowAll.html)| Shows all GameObjects.  
[TogglePicking](SceneVisibilityManager.TogglePicking.html)| Toggles the
picking ability of a GameObject.  
[ToggleVisibility](SceneVisibilityManager.ToggleVisibility.html)| Toggles the
visible state of a GameObject.  
  
### Events

[pickingChanged](SceneVisibilityManager-pickingChanged.html)| The event raised
whenever the picking state of a GameObject changes.  
---|---  
[visibilityChanged](SceneVisibilityManager-visibilityChanged.html)| The event
raised whenever the visibility of a GameObject changes.  
  
### Inherited Members

### Static Properties

[instance](ScriptableSingleton_1-instance.html)| Gets the instance of the
Singleton. Unity creates the Singleton instance when this property is accessed
for the first time. If you use the FilePathAttribute, then Unity loads the
data on the first access as well.  
---|---  
  
### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Protected Methods

[Save](ScriptableSingleton_1.Save.html)| Saves the current state of the
ScriptableSingleton.  
---|---  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
[CreateInstance](ScriptableObject.CreateInstance.html)| Creates an instance of
a scriptable object.  
[GetFilePath](ScriptableSingleton_1.GetFilePath.html)| Get the file path where
this ScriptableSingleton is saved to.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
### Messages

[Awake](ScriptableObject.Awake.html)| Called when an instance of
ScriptableObject is created.  
---|---  
[OnDestroy](ScriptableObject.OnDestroy.html)| This function is called when the
scriptable object will be destroyed.  
[OnDisable](ScriptableObject.OnDisable.html)| This function is called when the
scriptable object goes out of scope.  
[OnEnable](ScriptableObject.OnEnable.html)| This function is called when the
object is loaded.  
[OnValidate](ScriptableObject.OnValidate.html)| Editor-only function that
Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](ScriptableObject.Reset.html)| Reset to default values.  
  
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

