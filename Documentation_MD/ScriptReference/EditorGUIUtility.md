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

# EditorGUIUtility

class in UnityEditor

/

Inherits from:[GUIUtility](GUIUtility.html)

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

Miscellaneous helper stuff for [EditorGUI](EditorGUI.html).

### Static Properties

[currentViewWidth](EditorGUIUtility-currentViewWidth.html)| The width of the
GUI area for the current EditorWindow or other view. This Property should only
be accessed within an OnGUI call.  
---|---  
[editingTextField](EditorGUIUtility-editingTextField.html)| Is a text field
currently editing text?  
[fieldWidth](EditorGUIUtility-fieldWidth.html)| The minimum width in pixels
reserved for the fields of Editor GUI controls.  
[hierarchyMode](EditorGUIUtility-hierarchyMode.html)| Is the Editor GUI in
hierarchy mode?  
[isProSkin](EditorGUIUtility-isProSkin.html)| Is the user currently using the
pro skin? (Read Only)  
[labelWidth](EditorGUIUtility-labelWidth.html)| The width in pixels reserved
for labels of Editor GUI controls.  
[pixelsPerPoint](EditorGUIUtility-pixelsPerPoint.html)| The scale of GUI
points relative to screen pixels for the current viewThis value is the number
of screen pixels per point of interface space. For instance, 2.0 on retina
displays. Note that the value may differ from one view to the next if the
views are on monitors with different UI scales.  
[singleLineHeight](EditorGUIUtility-singleLineHeight.html)| Get the height
used for a single Editor control such as a one-line EditorGUI.TextField or
EditorGUI.Popup.  
[standardVerticalSpacing](EditorGUIUtility-standardVerticalSpacing.html)| Get
the height used by default for vertical spacing between controls.  
[systemCopyBuffer](EditorGUIUtility-systemCopyBuffer.html)| The system copy
buffer.  
[textFieldHasSelection](EditorGUIUtility-textFieldHasSelection.html)| True if
a text field currently has focused and the text in it is selected.  
[whiteTexture](EditorGUIUtility-whiteTexture.html)| Get a white texture.  
[wideMode](EditorGUIUtility-wideMode.html)| Is the Editor GUI currently in
wide mode?  
  
### Static Methods

[AddCursorRect](EditorGUIUtility.AddCursorRect.html)| Add a custom mouse
pointer to a control.  
---|---  
[CommandEvent](EditorGUIUtility.CommandEvent.html)| Creates an event that can
be sent to another window.  
[DrawColorSwatch](EditorGUIUtility.DrawColorSwatch.html)| Draw a color swatch.  
[DrawCurveSwatch](EditorGUIUtility.DrawCurveSwatch.html)| Draw a curve swatch.  
[DrawRegionSwatch](EditorGUIUtility.DrawRegionSwatch.html)| Draw swatch with a
filled region between two SerializedProperty curves.  
[FindTexture](EditorGUIUtility.FindTexture.html)| Get a texture from its
source filename.  
[GetBuiltinSkin](EditorGUIUtility.GetBuiltinSkin.html)| Get one of the built-
in GUI skins, which can be the game view, inspector or Scene view skin as
chosen by the parameter.  
[GetFlowLayoutedRects](EditorGUIUtility.GetFlowLayoutedRects.html)| Layout
list of string items left to right, top to bottom in the given area.  
[GetIconForObject](EditorGUIUtility.GetIconForObject.html)| Gets the custom
icon associated with an object. Only GameObjects and MonoScripts have
associated custom icons.  
[GetIconSize](EditorGUIUtility.GetIconSize.html)| Get the size that has been
set using SetIconSize.  
[GetMainWindowPosition](EditorGUIUtility.GetMainWindowPosition.html)| Returns
position of Unity Editor's main window.  
[GetObjectPickerControlID](EditorGUIUtility.GetObjectPickerControlID.html)|
The controlID of the currently showing object picker.  
[GetObjectPickerObject](EditorGUIUtility.GetObjectPickerObject.html)| The
object currently selected in the object picker.  
[HasObjectThumbnail](EditorGUIUtility.HasObjectThumbnail.html)| Does a given
class have per-object thumbnails?  
[IconContent](EditorGUIUtility.IconContent.html)| Fetch the GUIContent from
the Unity builtin resources with the given name.  
[IsDisplayReferencedByCameras](EditorGUIUtility.IsDisplayReferencedByCameras.html)|
Check if any enabled camera can render to a particular display.  
[Load](EditorGUIUtility.Load.html)| Load a built-in resource.  
[LoadRequired](EditorGUIUtility.LoadRequired.html)| Load a required built-in
resource.  
[LookLikeControls](EditorGUIUtility.LookLikeControls.html)| Make all EditorGUI
look like regular controls.  
[ObjectContent](EditorGUIUtility.ObjectContent.html)| Return a GUIContent
object with the name and icon of an Object.  
[PingObject](EditorGUIUtility.PingObject.html)| Ping an object in the Scene
like clicking it in an inspector.  
[PixelsToPoints](EditorGUIUtility.PixelsToPoints.html)| Convert from pixel
space to point space.  
[PointsToPixels](EditorGUIUtility.PointsToPixels.html)| Convert from point
space to pixel space.  
[QueueGameViewInputEvent](EditorGUIUtility.QueueGameViewInputEvent.html)| Send
an input event into the game.  
[SetIconForObject](EditorGUIUtility.SetIconForObject.html)| Sets a custom icon
to associate with a GameObject or MonoScript. The custom icon is displayed in
the Scene view and the Inspector.  
[SetIconSize](EditorGUIUtility.SetIconSize.html)| Set icons rendered as part
of GUIContent to be rendered at a specific size.  
[SetMainWindowPosition](EditorGUIUtility.SetMainWindowPosition.html)| Sets
position of Unity Editor's main window.  
[ShowObjectPicker](EditorGUIUtility.ShowObjectPicker.html)| Show the object
picker from code.  
[TrIconContent](EditorGUIUtility.TrIconContent.html)| Gets the GUIContent from
Unity built-in resources with the given information or creates a GUIContent
for a GUI element.The icon is loaded with a localized tooltip. Typically, the
icon from `Assets/Editor Default Resources/Icons` is fetched using the icon
name. Only the name of the icon, without the .png extension is needed.  
[TrTextContent](EditorGUIUtility.TrTextContent.html)| Gets the GUIContent from
the Unity built-in resources with the given key or creates a GUIContent for a
GUI element.The text and the tooltip are localized and loaded with an
icon.Typically, the icon from `Assets/Editor Default Resources/Icons` is
fetched using the icon name. Only the name of the icon, without the .png
extension is needed.  
[TrTextContentWithIcon](EditorGUIUtility.TrTextContentWithIcon.html)| Gets the
GUIContent from Unity built-in resources with the given information or creates
a GUIContent for a GUI element.The text and the tooltip are localized and
loaded with an icon.Typically, the icon from `Assets/Editor Default
Resources/Icons` is fetched using the icon name. Only the name of the icon,
without the .png extension is needed.If a message type is specified instead of
an icon or an icon name, the GUIContent.image is the icon associated with that
message type.  
  
### Inherited Members

### Static Properties

[hasModalWindow](GUIUtility-hasModalWindow.html)| A global property, which is
true if a ModalWindow is being displayed, false otherwise.  
---|---  
[hotControl](GUIUtility-hotControl.html)| The controlID of the current hot
control.  
[keyboardControl](GUIUtility-keyboardControl.html)| The controlID of the
control that has keyboard focus.  
[systemCopyBuffer](GUIUtility-systemCopyBuffer.html)| Get access to the
system-wide clipboard.  
  
### Static Methods

[AlignRectToDevice](GUIUtility.AlignRectToDevice.html)| Align a local space
rectangle to the pixel grid.  
---|---  
[ExitGUI](GUIUtility.ExitGUI.html)| Puts the GUI in a state that will prevent
all subsequent immediate mode GUI functions from evaluating for the remainder
of the GUI loop by throwing an ExitGUIException.  
[GetControlID](GUIUtility.GetControlID.html)| Get a unique ID for a control.  
[GetStateObject](GUIUtility.GetStateObject.html)| Get a state object from a
controlID.  
[GUIToScreenPoint](GUIUtility.GUIToScreenPoint.html)| Convert a point from GUI
position to screen space.  
[GUIToScreenRect](GUIUtility.GUIToScreenRect.html)| Convert a rect from GUI
position to screen space.  
[QueryStateObject](GUIUtility.QueryStateObject.html)| Get an existing state
object from a controlID.  
[RotateAroundPivot](GUIUtility.RotateAroundPivot.html)| Helper function to
rotate the GUI around a point.  
[ScaleAroundPivot](GUIUtility.ScaleAroundPivot.html)| Helper function to scale
the GUI around a point.  
[ScreenToGUIPoint](GUIUtility.ScreenToGUIPoint.html)| Convert a point from
screen space to GUI position.  
[ScreenToGUIRect](GUIUtility.ScreenToGUIRect.html)| Convert a rect from screen
space to GUI position.  
  
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

