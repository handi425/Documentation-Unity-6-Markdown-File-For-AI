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

# EditorApplication

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

Main Application class.

### Static Properties

[applicationContentsPath](EditorApplication-applicationContentsPath.html)|
Path to the Unity editor contents folder. (Read Only)  
---|---  
[applicationPath](EditorApplication-applicationPath.html)| Gets the path to
the Unity Editor application. (Read Only)  
[contextualPropertyMenu](EditorApplication-contextualPropertyMenu.html)|
Callback raised whenever the user context-clicks on a property in an
Inspector.  
[delayCall](EditorApplication-delayCall.html)| Delegate which is called once
after all inspectors update.  
[hierarchyWindowItemOnGUI](EditorApplication-hierarchyWindowItemOnGUI.html)|
Delegate for OnGUI events for every visible list item in the HierarchyWindow.  
[isCompiling](EditorApplication-isCompiling.html)| Is editor currently
compiling scripts? (Read Only)  
[isCreateFromTemplate](EditorApplication-isCreateFromTemplate.html)| Returns
true if the current project was created from a template project.  
[isFocused](EditorApplication-isFocused.html)| Whether the Editor is the
focused window of the operating system. (Read Only)  
[isPaused](EditorApplication-isPaused.html)| Whether the Editor is paused.  
[isPlaying](EditorApplication-isPlaying.html)| Whether the Editor is in Play
mode.  
[isPlayingOrWillChangePlaymode](EditorApplication-
isPlayingOrWillChangePlaymode.html)| Editor application state which is true
only when the Editor is currently in or about to enter Play mode. (Read Only)  
[isRemoteConnected](EditorApplication-isRemoteConnected.html)| Is editor
currently connected to Unity Remote 4 client app.  
[isTemporaryProject](EditorApplication-isTemporaryProject.html)| Returns true
if the current project was created as a temporary project.  
[isUpdating](EditorApplication-isUpdating.html)| True if the Editor is
currently refreshing the AssetDatabase.  
[modifierKeysChanged](EditorApplication-modifierKeysChanged.html)| Delegate
for changed keyboard modifier keys.  
[projectWindowItemInstanceOnGUI](EditorApplication-
projectWindowItemInstanceOnGUI.html)| Delegate for OnGUI events for every
visible list item in the ProjectWindow.  
[projectWindowItemOnGUI](EditorApplication-projectWindowItemOnGUI.html)|
Delegate for OnGUI events for every visible list item in the ProjectWindow.  
[searchChanged](EditorApplication-searchChanged.html)| Callback raised
whenever the contents of a window's search box are changed.  
[timeSinceStartup](EditorApplication-timeSinceStartup.html)| The time since
the editor was started. (Read Only)  
[update](EditorApplication-update.html)| Delegate for generic updates.  
  
### Static Methods

[Beep](EditorApplication.Beep.html)| Plays system beep sound.  
---|---  
[DirtyHierarchyWindowSorting](EditorApplication.DirtyHierarchyWindowSorting.html)|
Set the hierarchy sorting method as dirty.  
[EnterPlaymode](EditorApplication.EnterPlaymode.html)| Switches the editor to
Play mode.  
[ExecuteMenuItem](EditorApplication.ExecuteMenuItem.html)| Invokes the menu
item in the specified path.  
[Exit](EditorApplication.Exit.html)| Exit the Unity editor application.  
[ExitPlaymode](EditorApplication.ExitPlaymode.html)| Switches the editor to
Edit mode.  
[LockReloadAssemblies](EditorApplication.LockReloadAssemblies.html)| Prevents
loading of assemblies when it is inconvenient.  
[OpenProject](EditorApplication.OpenProject.html)| Open another project.  
[QueuePlayerLoopUpdate](EditorApplication.QueuePlayerLoopUpdate.html)|
Normally, a player loop update will occur in the editor when the Scene has
been modified. This method allows you to queue a player loop update regardless
of whether the Scene has been modified.  
[RepaintHierarchyWindow](EditorApplication.RepaintHierarchyWindow.html)| Can
be used to ensure repaint of the HierarchyWindow.  
[RepaintProjectWindow](EditorApplication.RepaintProjectWindow.html)| Can be
used to ensure repaint of the ProjectWindow.  
[SetTemporaryProjectKeepPath](EditorApplication.SetTemporaryProjectKeepPath.html)|
Sets the path that Unity should store the current temporary project at, when
the project is closed.  
[Step](EditorApplication.Step.html)| Perform a single frame step.  
[UnlockReloadAssemblies](EditorApplication.UnlockReloadAssemblies.html)| Must
be called after LockReloadAssemblies, to reenable loading of assemblies.  
[UpdateMainWindowTitle](EditorApplication.UpdateMainWindowTitle.html)| Force
Unity Editor to update its window title. This function is automatically called
when a new scene is loaded or when the editor starts. A user having register a
callback on EditorApplication.updateMainWindowTitle can call this function to
force an update of the title.  
  
### Events

[focusChanged](EditorApplication-focusChanged.html)| Raises when the Editor
gets or loses focus in the operating system.  
---|---  
[hierarchyChanged](EditorApplication-hierarchyChanged.html)| Event that is
raised when an object or group of objects in the hierarchy changes.  
[pauseStateChanged](EditorApplication-pauseStateChanged.html)| Event that is
raised whenever the Editor's pause state changes.  
[playModeStateChanged](EditorApplication-playModeStateChanged.html)| Event
that is raised whenever the Editor's play mode state changes.  
[projectChanged](EditorApplication-projectChanged.html)| Event that is raised
whenever the state of the project changes.  
[quitting](EditorApplication-quitting.html)| Unity raises this event when the
editor application is quitting.  
[updateMainWindowTitle](EditorApplication-updateMainWindowTitle.html)|
Register a custom callback to specify how the Unity Editor title can be
generated. Unity will trigger this callback when a new scene is loaded , when
Unity starts or when EditorApplication.UpdateMainWindowTitle is called.  
[wantsToQuit](EditorApplication-wantsToQuit.html)| Unity raises this event
when the editor application wants to quit.  
  
### Delegates

[CallbackFunction](EditorApplication.CallbackFunction.html)| Delegate to be
called from EditorApplication callbacks.  
---|---  
[HierarchyWindowItemCallback](EditorApplication.HierarchyWindowItemCallback.html)|
Delegate to be called for every visible list item in the HierarchyWindow on
every OnGUI event.  
[ProjectWindowItemCallback](EditorApplication.ProjectWindowItemCallback.html)|
Delegate to be called for every visible list item in the ProjectWindow on
every OnGUI event. Use this if you if you want to extend the functionality of
the Project window. For example, to display information or tools relating to
the assets that are visible.  
[ProjectWindowItemInstanceCallback](EditorApplication.ProjectWindowItemInstanceCallback.html)|
Delegate to be called for every visible list item in the ProjectWindow on
every OnGUI event. Use this if you if you want to extend the functionality of
the Project window. For example, to display information or tools relating to
the assets or sub-assets that are visible.  
[SerializedPropertyCallbackFunction](EditorApplication.SerializedPropertyCallbackFunction.html)|
Delegate to be called from EditorApplication contextual inspector callbacks.  
  
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

