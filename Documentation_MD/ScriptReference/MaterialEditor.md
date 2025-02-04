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

# MaterialEditor

class in UnityEditor

/

Inherits from:[Editor](Editor.html)

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

The Unity Material Editor.

Extend this class to write your own custom material editor. For more detailed
information see the [Custom Material Editor](../Manual/SL-CustomEditor.html)
section of the [ShaderLab reference](../Manual/SL-Shader.html).

### Static Properties

[kMiniTextureFieldLabelIndentLevel](MaterialEditor-
kMiniTextureFieldLabelIndentLevel.html)| Useful for indenting shader
properties that need the same indent as mini texture field.  
---|---  
  
### Properties

[customShaderGUI](MaterialEditor-customShaderGUI.html)| Returns the custom
ShaderGUI implemented by the shader.  
---|---  
[isVisible](MaterialEditor-isVisible.html)| Is the current material expanded.  
  
### Public Methods

[Awake](MaterialEditor.Awake.html)| Called when the Editor is woken up.  
---|---  
[BeginAnimatedCheck](MaterialEditor.BeginAnimatedCheck.html)| Creates a
Property wrapper, useful for making regular GUI controls work with
MaterialProperty.  
[ColorProperty](MaterialEditor.ColorProperty.html)| Draw a property field for
a color shader property.  
[CreatePreview](MaterialEditor.CreatePreview.html)| See Editor.CreatePreview.  
[DefaultPreviewGUI](MaterialEditor.DefaultPreviewGUI.html)| Default handling
of preview area for materials.  
[DefaultPreviewSettingsGUI](MaterialEditor.DefaultPreviewSettingsGUI.html)|
Default toolbar for material preview area.  
[DefaultShaderProperty](MaterialEditor.DefaultShaderProperty.html)| Handles UI
for one shader property ignoring any custom drawers.  
[DoubleSidedGIField](MaterialEditor.DoubleSidedGIField.html)| Display UI for
editing a material's Double Sided Global Illumination setting. Returns true if
the UI is indeed displayed i.e. the material supports the Double Sided Global
Illumination setting. +Additional resources: Material.doubleSidedGI.  
[EmissionEnabledProperty](MaterialEditor.EmissionEnabledProperty.html)| This
function will draw the UI for controlling whether emission is enabled or not
on a material.  
[EnableInstancingField](MaterialEditor.EnableInstancingField.html)| Display UI
for editing material's render queue setting.  
[EndAnimatedCheck](MaterialEditor.EndAnimatedCheck.html)| Ends a Property
wrapper started with BeginAnimatedCheck.  
[FloatProperty](MaterialEditor.FloatProperty.html)| Draw a property field for
a float shader property.  
[GetPropertyHeight](MaterialEditor.GetPropertyHeight.html)| Calculate height
needed for the property.  
[GetTexturePropertyCustomArea](MaterialEditor.GetTexturePropertyCustomArea.html)|
Returns the free rect below the label and before the large thumb object field.
Is used for e.g. tiling and offset properties.  
[HasPreviewGUI](MaterialEditor.HasPreviewGUI.html)| Can this component be
Previewed in its current state?  
[HelpBoxWithButton](MaterialEditor.HelpBoxWithButton.html)| Make a help box
with a message and button. Returns true, if button was pressed.  
[IntegerProperty](MaterialEditor.IntegerProperty.html)| Draw a property field
for an integer shader property.  
[IsInstancingEnabled](MaterialEditor.IsInstancingEnabled.html)| Determines
whether the Enable Instancing checkbox is checked.  
[LightmapEmissionFlagsProperty](MaterialEditor.LightmapEmissionFlagsProperty.html)|
Draws the UI for setting the global illumination flag of a material.  
[LightmapEmissionProperty](MaterialEditor.LightmapEmissionProperty.html)| This
function will draw the UI for the lightmap emission property. (None, Realtime,
baked)Additional resources: MaterialLightmapFlags.  
[OnDisable](MaterialEditor.OnDisable.html)| Called when the editor is
disabled, if overridden please call the base OnDisable() to ensure that the
material inspector is set up properly.  
[OnEnable](MaterialEditor.OnEnable.html)| Called when the editor is enabled,
if overridden please call the base OnEnable() to ensure that the material
inspector is set up properly.  
[OnInspectorGUI](MaterialEditor.OnInspectorGUI.html)| Implement specific
MaterialEditor GUI code here. If you want to simply extend the existing editor
call the base OnInspectorGUI () before doing any custom GUI code.  
[OnPreviewGUI](MaterialEditor.OnPreviewGUI.html)| Custom preview for Image
component.  
[PropertiesChanged](MaterialEditor.PropertiesChanged.html)| Whenever a
material property is changed call this function. This will rebuild the
inspector and validate the properties.  
[PropertiesDefaultGUI](MaterialEditor.PropertiesDefaultGUI.html)| Default
rendering of shader properties.  
[PropertiesGUI](MaterialEditor.PropertiesGUI.html)| Render the standard
material properties. This method will either render properties using a
ShaderGUI instance if found otherwise it uses PropertiesDefaultGUI.  
[RangeProperty](MaterialEditor.RangeProperty.html)| Draw a range slider for a
range shader property.  
[RegisterPropertyChangeUndo](MaterialEditor.RegisterPropertyChangeUndo.html)|
Call this when you change a material property. It will add an undo for the
action.  
[RenderQueueField](MaterialEditor.RenderQueueField.html)| Display UI for
editing material's render queue setting.  
[RequiresConstantRepaint](MaterialEditor.RequiresConstantRepaint.html)| Does
this edit require to be repainted constantly in its current state?  
[SetDefaultGUIWidths](MaterialEditor.SetDefaultGUIWidths.html)| Set
EditorGUIUtility.fieldWidth and labelWidth to the default values that
PropertiesGUI uses.  
[SetShader](MaterialEditor.SetShader.html)| Set the shader of the material.  
[ShaderProperty](MaterialEditor.ShaderProperty.html)| Handes UI for one shader
property.  
[TextureCompatibilityWarning](MaterialEditor.TextureCompatibilityWarning.html)|
Checks if particular property has incorrect type of texture specified by the
material, displays appropriate warning and suggests the user to automatically
fix the problem.  
[TextureProperty](MaterialEditor.TextureProperty.html)| Draw a property field
for a texture shader property.  
[TexturePropertyMiniThumbnail](MaterialEditor.TexturePropertyMiniThumbnail.html)|
Draw a property field for a texture shader property that only takes up a
single line height.  
[TexturePropertySingleLine](MaterialEditor.TexturePropertySingleLine.html)|
Method for showing a texture property control with additional inlined
properites.  
[TexturePropertyTwoLines](MaterialEditor.TexturePropertyTwoLines.html)| Method
for showing a compact layout of properties.  
[TexturePropertyWithHDRColor](MaterialEditor.TexturePropertyWithHDRColor.html)|
Method for showing a texture property control with a HDR color field and its
color brightness float field.  
[TextureScaleOffsetProperty](MaterialEditor.TextureScaleOffsetProperty.html)|
Draws tiling and offset properties for a texture.  
[VectorProperty](MaterialEditor.VectorProperty.html)| Draw a property field
for a vector shader property.  
  
### Protected Methods

[OnShaderChanged](MaterialEditor.OnShaderChanged.html)| A callback that is
invoked when a Material's Shader is changed in the Inspector.  
---|---  
  
### Static Methods

[ApplyMaterialPropertyDrawers](MaterialEditor.ApplyMaterialPropertyDrawers.html)|
Apply initial MaterialPropertyDrawer values.  
---|---  
[BeginProperty](MaterialEditor.BeginProperty.html)| Creates a wrapper enabling
the Unity Editor to display GUI controls for the property.  
[EndProperty](MaterialEditor.EndProperty.html)| Closes a property wrapper that
begins with MaterialEditor.BeginProperty.  
[FixupEmissiveFlag](MaterialEditor.FixupEmissiveFlag.html)| Returns a properly
set global illlumination flag based on the passed in flag and the given color.  
[GetDefaultPropertyHeight](MaterialEditor.GetDefaultPropertyHeight.html)|
Calculate height needed for the property, ignoring custom drawers.  
[GetFlexibleRectBetweenFieldAndRightEdge](MaterialEditor.GetFlexibleRectBetweenFieldAndRightEdge.html)|
Utility method for GUI layouting ShaderGUI. Used e.g for the rect after a left
aligned Color field.  
[GetFlexibleRectBetweenLabelAndField](MaterialEditor.GetFlexibleRectBetweenLabelAndField.html)|
Utility method for GUI layouting ShaderGUI.  
[GetLeftAlignedFieldRect](MaterialEditor.GetLeftAlignedFieldRect.html)|
Utility method for GUI layouting ShaderGUI.  
[GetMaterialProperties](MaterialEditor.GetMaterialProperties.html)| Get shader
property information of the materials you pass in.  
[GetMaterialProperty](MaterialEditor.GetMaterialProperty.html)| Get
information about a single shader property.  
[GetMaterialPropertyNames](MaterialEditor.GetMaterialPropertyNames.html)| Gets
the shader property names of the materials you pass in.  
[GetRectAfterLabelWidth](MaterialEditor.GetRectAfterLabelWidth.html)| Utility
method for GUI layouting ShaderGUI. This is the rect after the label which can
be used for multiple properties. The input rect can be fetched by calling:
EditorGUILayout.GetControlRect.  
[GetRightAlignedFieldRect](MaterialEditor.GetRightAlignedFieldRect.html)|
Utility method for GUI layouting ShaderGUI.  
  
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
[OnInteractivePreviewGUI](Editor.OnInteractivePreviewGUI.html)| Implement to
create your own interactive custom preview. Interactive custom previews are
used in the preview area of the inspector and the object selector.  
[OnPreviewSettings](Editor.OnPreviewSettings.html)| Override this method if
you want to show custom controls in the preview header.  
[RenderStaticPreview](Editor.RenderStaticPreview.html)| Override this method
if you want to render a static preview.  
[Repaint](Editor.Repaint.html)| Redraw any inspectors that shows this editor.  
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
[OnDestroy](ScriptableObject.OnDestroy.html)| This function is called when the
scriptable object will be destroyed.  
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

