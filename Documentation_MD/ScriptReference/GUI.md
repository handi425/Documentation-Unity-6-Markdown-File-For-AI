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

# GUI

class in UnityEngine

/

Implemented in:[UnityEngine.IMGUIModule](UnityEngine.IMGUIModule.html)

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

The GUI class is the interface for Unity's GUI with manual positioning.

  
Additional resources: [GUI tutorial](../Manual/GUIScriptingGuide.html).

### Static Properties

[backgroundColor](GUI-backgroundColor.html)| Global tinting color for all
background elements rendered by the GUI.  
---|---  
[changed](GUI-changed.html)| Returns true if any controls changed the value of
the input data.  
[color](GUI-color.html)| Applies a global tint to the GUI. The tint affects
backgrounds and text colors.  
[contentColor](GUI-contentColor.html)| Tinting color for all text rendered by
the GUI.  
[depth](GUI-depth.html)| The sorting depth of the currently executing GUI
behaviour.  
[enabled](GUI-enabled.html)| Is the GUI enabled?  
[matrix](GUI-matrix.html)| The GUI transform matrix.  
[skin](GUI-skin.html)| The global skin to use.  
[tooltip](GUI-tooltip.html)| The tooltip of the control the mouse is currently
over, or which has keyboard focus. (Read Only).  
  
### Static Methods

[BeginGroup](GUI.BeginGroup.html)| Begin a group. Must be matched with a call
to EndGroup.  
---|---  
[BeginScrollView](GUI.BeginScrollView.html)| Begin a scrolling view inside
your GUI.  
[Box](GUI.Box.html)| Create a Box on the GUI Layer.  
[BringWindowToBack](GUI.BringWindowToBack.html)| Bring a specific window to
back of the floating windows.  
[BringWindowToFront](GUI.BringWindowToFront.html)| Bring a specific window to
front of the floating windows.  
[Button](GUI.Button.html)| Make a single press button. The user clicks them
and something happens immediately.  
[DragWindow](GUI.DragWindow.html)| Make a window draggable.  
[DrawTexture](GUI.DrawTexture.html)| Draw a texture within a rectangle.  
[DrawTextureWithTexCoords](GUI.DrawTextureWithTexCoords.html)| Draw a texture
within a rectangle with the given texture coordinates.  
[EndGroup](GUI.EndGroup.html)| End a group.  
[EndScrollView](GUI.EndScrollView.html)| Ends a scrollview started with a call
to BeginScrollView.  
[FocusControl](GUI.FocusControl.html)| Move keyboard focus to a named control.  
[FocusWindow](GUI.FocusWindow.html)| Make a window become the active window.  
[GetNameOfFocusedControl](GUI.GetNameOfFocusedControl.html)| Get the name of
named control that has focus.  
[HorizontalScrollbar](GUI.HorizontalScrollbar.html)| Make a horizontal
scrollbar. Scrollbars are what you use to scroll through a document. Most
likely, you want to use scrollViews instead.  
[HorizontalSlider](GUI.HorizontalSlider.html)| A horizontal slider the user
can drag to change a value between a min and a max.  
[Label](GUI.Label.html)| Make a text or texture label on screen.  
[ModalWindow](GUI.ModalWindow.html)| Show a Modal Window.  
[PasswordField](GUI.PasswordField.html)| Make a text field where the user can
enter a password.  
[RepeatButton](GUI.RepeatButton.html)| Make a button that is active as long as
the user holds it down.  
[ScrollTo](GUI.ScrollTo.html)| Scrolls all enclosing scrollviews so they try
to make position visible.  
[SelectionGrid](GUI.SelectionGrid.html)| Make a grid of buttons.  
[SetNextControlName](GUI.SetNextControlName.html)| Set the name of the next
control.  
[TextArea](GUI.TextArea.html)| Make a Multi-line text area where the user can
edit a string.  
[TextField](GUI.TextField.html)| Make a single-line text field where the user
can edit a string.  
[Toggle](GUI.Toggle.html)| Make an on/off toggle button.  
[Toolbar](GUI.Toolbar.html)| Make a toolbar.  
[UnfocusWindow](GUI.UnfocusWindow.html)| Remove focus from all windows.  
[VerticalScrollbar](GUI.VerticalScrollbar.html)| Make a vertical scrollbar.
Scrollbars are what you use to scroll through a document. Most likely, you
want to use scrollViews instead.  
[VerticalSlider](GUI.VerticalSlider.html)| A vertical slider the user can drag
to change a value between a min and a max.  
[Window](GUI.Window.html)| Make a popup window.  
  
### Delegates

[WindowFunction](GUI.WindowFunction.html)| Callback to draw GUI within a
window (used with GUI.Window).  
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

