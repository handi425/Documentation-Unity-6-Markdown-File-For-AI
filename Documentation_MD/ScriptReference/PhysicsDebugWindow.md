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

# PhysicsDebugWindow

class in UnityEditor

/

Inherits from:[EditorWindow](EditorWindow.html)

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

Displays the Physics Debug Visualization options.  
  
The Physics Debug Visualization is only displayed if this window is visible.  
  
Additional resources:
[PhysicsVisualizationSettings](PhysicsVisualizationSettings.html).

### Inherited Members

### Static Properties

[focusedWindow](EditorWindow-focusedWindow.html)| The EditorWindow which
currently has keyboard focus. (Read Only)  
---|---  
[mouseOverWindow](EditorWindow-mouseOverWindow.html)| The EditorWindow
currently under the mouse cursor. (Read Only)  
  
### Properties

[autoRepaintOnSceneChange](EditorWindow-autoRepaintOnSceneChange.html)| Enable
this property to automatically repaint the window when the SceneView is
modified.  
---|---  
[dataModeController](EditorWindow-dataModeController.html)| An instance of
IDataModeController to handle DataMode functionalities for the current window.  
[docked](EditorWindow-docked.html)| Returns true if EditorWindow is docked.  
[hasFocus](EditorWindow-hasFocus.html)| Returns true if EditorWindow is
focused.  
[hasUnsavedChanges](EditorWindow-hasUnsavedChanges.html)| This property
specifies whether the Editor prompts the user to save or discard unsaved
changes before the window closes.  
[maximized](EditorWindow-maximized.html)| Whether or not this window is
maximized?  
[maxSize](EditorWindow-maxSize.html)| The maximum size of this window when it
is floating or modal. The maximum size is not used when the window is docked.  
[minSize](EditorWindow-minSize.html)| The minimum size of this window when it
is floating or modal. The minimum size is not used when the window is docked.  
[overlayCanvas](EditorWindow-overlayCanvas.html)| The OverlayCanvas for this
window.  
[position](EditorWindow-position.html)| The desired position of the window in
screen space.  
[rootVisualElement](EditorWindow-rootVisualElement.html)| Retrieves the root
visual element of this window hierarchy.  
[saveChangesMessage](EditorWindow-saveChangesMessage.html)| The message that
displays to the user if they are prompted to save  
[titleContent](EditorWindow-titleContent.html)| The GUIContent used for
drawing the title of EditorWindows.  
[wantsLessLayoutEvents](EditorWindow-wantsLessLayoutEvents.html)| Specifies
whether a layout pass is performed before all user events (for example,
EventType.MouseDown or EventType.KeyDown), or is only performed before repaint
events.  
[wantsMouseEnterLeaveWindow](EditorWindow-wantsMouseEnterLeaveWindow.html)|
Checks whether MouseEnterWindow and MouseLeaveWindow events are received in
the GUI in this Editor window.  
[wantsMouseMove](EditorWindow-wantsMouseMove.html)| Checks whether MouseMove
events are received in the GUI in this Editor window.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[BeginWindows](EditorWindow.BeginWindows.html)| Mark the beginning area of all
popup windows.  
---|---  
[Close](EditorWindow.Close.html)| Close the editor window.  
[DiscardChanges](EditorWindow.DiscardChanges.html)| Discards unsaved changes
to the contents of the window.  
[EndWindows](EditorWindow.EndWindows.html)| Close a window group started with
EditorWindow.BeginWindows.  
[Focus](EditorWindow.Focus.html)| Moves keyboard focus to another
EditorWindow.  
[GetExtraPaneTypes](EditorWindow.GetExtraPaneTypes.html)| Gets the extra panes
associated with the window.  
[RemoveNotification](EditorWindow.RemoveNotification.html)| Stop showing
notification message.  
[Repaint](EditorWindow.Repaint.html)| Make the window repaint.  
[SaveChanges](EditorWindow.SaveChanges.html)| Performs a save action on the
contents of the window.  
[SendEvent](EditorWindow.SendEvent.html)| Sends an Event to a window.  
[Show](EditorWindow.Show.html)| Show the EditorWindow window.  
[ShowAsDropDown](EditorWindow.ShowAsDropDown.html)| Shows a window with
dropdown behaviour and styling.  
[ShowAuxWindow](EditorWindow.ShowAuxWindow.html)| Show the editor window in
the auxiliary window.  
[ShowModal](EditorWindow.ShowModal.html)| Show modal editor window.  
[ShowModalUtility](EditorWindow.ShowModalUtility.html)| Shows the EditorWindow
as a floating modal window.  
[ShowNotification](EditorWindow.ShowNotification.html)| Show a notification
message.  
[ShowPopup](EditorWindow.ShowPopup.html)| Shows an Editor window using popup-
style framing.  
[ShowTab](EditorWindow.ShowTab.html)| Shows a docked Editor window.  
[ShowUtility](EditorWindow.ShowUtility.html)| Show the EditorWindow as a
floating utility window.  
[TryGetOverlay](EditorWindow.TryGetOverlay.html)| Get an Overlay with matching
ID from an EditorWindow canvas.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Protected Methods

[OnBackingScaleFactorChanged](EditorWindow.OnBackingScaleFactorChanged.html)|
Called when the UI scaling for this EditorWindow is changed.  
---|---  
  
### Static Methods

[CreateWindow](EditorWindow.CreateWindow.html)| Creates an EditorWindow of
type T.  
---|---  
[FocusWindowIfItsOpen](EditorWindow.FocusWindowIfItsOpen.html)| Focuses the
first found EditorWindow of specified type if it is open.  
[GetWindow](EditorWindow.GetWindow.html)| Returns the first EditorWindow of
type windowType which is currently on the screen.  
[GetWindowWithRect](EditorWindow.GetWindowWithRect.html)| Returns the first
EditorWindow of type t which is currently on the screen.  
[HasOpenInstances](EditorWindow.HasOpenInstances.html)| Checks if an editor
window is open.  
[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
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
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
### Messages

[Awake](EditorWindow.Awake.html)| Called as the new window is opened.  
---|---  
[CreateGUI](EditorWindow.CreateGUI.html)|  CreateGUI is called when the
EditorWindow's rootVisualElement is ready to be populated.  
[hasUnsavedChanges](EditorWindow-hasUnsavedChanges.html)| This property
specifies whether the Editor prompts the user to save or discard unsaved
changes before the window closes.  
[OnBecameInvisible](EditorWindow.OnBecameInvisible.html)| Called after the
window is removed from a container view, or is no longer visible within a
tabbed collection of EditorWindow.  
[OnBecameVisible](EditorWindow.OnBecameVisible.html)| Called after the window
is added to a container view.  
[OnDestroy](EditorWindow.OnDestroy.html)| OnDestroy is called to close the
EditorWindow window.  
[OnFocus](EditorWindow.OnFocus.html)| Called when the window gets keyboard
focus.  
[OnGUI](EditorWindow.OnGUI.html)| Implement your own editor GUI here.  
[OnHierarchyChange](EditorWindow.OnHierarchyChange.html)| Handler for message
that is sent when an object or group of objects in the hierarchy changes.  
[OnInspectorUpdate](EditorWindow.OnInspectorUpdate.html)| OnInspectorUpdate is
called at 10 frames per second to give the inspector a chance to update.  
[OnLostFocus](EditorWindow.OnLostFocus.html)| Called when the window loses
keyboard focus.  
[OnProjectChange](EditorWindow.OnProjectChange.html)| Handler for message that
is sent whenever the state of the project changes.  
[OnSelectionChange](EditorWindow.OnSelectionChange.html)| Called whenever the
selection has changed.  
[saveChangesMessage](EditorWindow-saveChangesMessage.html)| The message that
displays to the user if they are prompted to save  
[Update](EditorWindow.Update.html)| Called multiple times per second on all
visible windows.  
[Awake](ScriptableObject.Awake.html)| Called when an instance of
ScriptableObject is created.  
[OnDestroy](ScriptableObject.OnDestroy.html)| This function is called when the
scriptable object will be destroyed.  
[OnDisable](ScriptableObject.OnDisable.html)| This function is called when the
scriptable object goes out of scope.  
[OnEnable](ScriptableObject.OnEnable.html)| This function is called when the
object is loaded.  
[OnValidate](ScriptableObject.OnValidate.html)| Editor-only function that
Unity calls when the script is loaded or a value changes in the Inspector.  
[Reset](ScriptableObject.Reset.html)| Reset to default values.  
  
### Events

[windowFocusChanged](EditorWindow-windowFocusChanged.html)| Called whenever
the focused editor window is changed.  
---|---  
  
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

