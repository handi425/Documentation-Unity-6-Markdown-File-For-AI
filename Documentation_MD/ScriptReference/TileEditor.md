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

# TileEditor

class in UnityEditor

/

Inherits from:[TileBaseEditor](TileBaseEditor.html)

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

Default editor for [Tile](WSA.Tile.html) assets.

### Public Methods

[OnInspectorGUI](TileEditor.OnInspectorGUI.html)| Draws the default Tile
Inspector GUI.  
---|---  
[RenderStaticPreview](TileEditor.RenderStaticPreview.html)| Creates a texture
preview for rendering the Tile asset preview.  
  
### Inherited Members

### Properties

[hasUnsavedChanges](Editor-hasUnsavedChanges.html)| This property specifies
whether the Editor prompts the user to save or discard unsaved changes before
the Inspector gets rebuilt.  
---|---  
[saveChangesMessage](Editor-saveChangesMessage.html)| The message that
displays to the user if they are prompted to save.  
[serializedObject](Editor-serializedObject.html)| A SerializedObject
representing the object or objects being inspected.  
[target](Editor-target.html)| The object being inspected.  
[targets](Editor-targets.html)| An array of all the object being inspected.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[CreateInspectorGUI](Editor.CreateInspectorGUI.html)| Implement this method to
make a custom UIElements inspector.  
---|---  
[CreatePreview](Editor.CreatePreview.html)| Implement this method to make a
custom UIElements inspector preview.  
[DiscardChanges](Editor.DiscardChanges.html)| Discards unsaved changes to the
contents of the editor.  
[DrawDefaultInspector](Editor.DrawDefaultInspector.html)| Draws the built-in
Inspector.  
[DrawHeader](Editor.DrawHeader.html)| Call this function to draw the header of
the editor.  
[DrawPreview](Editor.DrawPreview.html)| The first entry point for Preview
Drawing.  
[GetInfoString](Editor.GetInfoString.html)| Implement this method to show
asset information on top of the asset preview.  
[GetPreviewTitle](Editor.GetPreviewTitle.html)| Override this method if you
want to change the label of the Preview area.  
[HasPreviewGUI](Editor.HasPreviewGUI.html)| Override this method in subclasses
if you implement OnPreviewGUI.  
[OnInteractivePreviewGUI](Editor.OnInteractivePreviewGUI.html)| Implement to
create your own interactive custom preview. Interactive custom previews are
used in the preview area of the inspector and the object selector.  
[OnPreviewGUI](Editor.OnPreviewGUI.html)| Creates a custom preview for the
preview area of the Inspector, the headers of the primary Editor, and the
object selector.You must implement Editor.HasPreviewGUI for this method to be
called.  
[OnPreviewSettings](Editor.OnPreviewSettings.html)| Override this method if
you want to show custom controls in the preview header.  
[Repaint](Editor.Repaint.html)| Redraw any inspectors that shows this editor.  
[RequiresConstantRepaint](Editor.RequiresConstantRepaint.html)| Checks if this
editor requires constant repaints in its current state.  
[SaveChanges](Editor.SaveChanges.html)| Performs a save action on the contents
of the editor.  
[UseDefaultMargins](Editor.UseDefaultMargins.html)| Override this method in
subclasses to return false if you don't want default margins.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Protected Methods

[ShouldHideOpenButton](Editor.ShouldHideOpenButton.html)| Returns the
visibility setting of the "open" button in the Inspector.  
---|---  
  
### Static Methods

[CreateCachedEditor](Editor.CreateCachedEditor.html)| On return previousEditor
is an editor for targetObject or targetObjects. The function either returns if
the editor is already tracking the objects, or destroys the previous editor
and creates a new one.  
---|---  
[CreateCachedEditorWithContext](Editor.CreateCachedEditorWithContext.html)|
Creates a cached editor using a context object.  
[CreateEditor](Editor.CreateEditor.html)| Make a custom editor for
targetObject or targetObjects.  
[CreateEditorWithContext](Editor.CreateEditorWithContext.html)| Make a custom
editor for targetObject or targetObjects with a context object.  
[DrawFoldoutInspector](Editor.DrawFoldoutInspector.html)| Draws the inspector
GUI with a foldout header for target.  
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

[HasFrameBounds](Editor.HasFrameBounds.html)| Validates whether custom bounds
can be calculated for this Editor.  
---|---  
[OnGetFrameBounds](Editor.OnGetFrameBounds.html)| Gets custom bounds for the
target of this editor.  
[OnSceneGUI](Editor.OnSceneGUI.html)| Enables the Editor to handle an event in
the Scene view.  
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

[finishedDefaultHeaderGUI](Editor-finishedDefaultHeaderGUI.html)| An event
raised while drawing the header of the Inspector window, after the default
header items have been drawn.  
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

