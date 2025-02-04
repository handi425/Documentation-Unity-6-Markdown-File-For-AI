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

# TerrainPaintToolWithOverlaysBase

class in UnityEditor.TerrainTools

/

Inherits from:[EditorTools.EditorTool](EditorTools.EditorTool.html)

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

The abstract class that TerrainPaintToolWithOverlays inherits from.

Contains fields that can be overridden when you implement your own terrain
painting tools to display in Terrain overlays. When you create custom Terrain
Tools, they must inherit from the
[TerrainPaintToolWithOverlays<T0>](TerrainTools.TerrainPaintToolWithOverlays_1.html)
class rather than this class.

### Properties

[Category](TerrainTools.TerrainPaintToolWithOverlaysBase.Category.html)| The
TerrainCategory that the Terrain Tool belongs to.  
---|---  
[HasBrushAttributes](TerrainTools.TerrainPaintToolWithOverlaysBase.HasBrushAttributes.html)|
True if the Terrain Tool has brush attributes, false otherwise.  
[HasBrushMask](TerrainTools.TerrainPaintToolWithOverlaysBase.HasBrushMask.html)|
True if Terrain Tool has brush masks, false otherwise.  
[HasToolSettings](TerrainTools.TerrainPaintToolWithOverlaysBase.HasToolSettings.html)|
True if Terrain Tool has custom settings, false otherwise.  
[IconIndex](TerrainTools.TerrainPaintToolWithOverlaysBase.IconIndex.html)| The
index at which you should place the Terrain Tool in the Terrain Tools overlay.  
[OffIcon](TerrainTools.TerrainPaintToolWithOverlaysBase.OffIcon.html)| The
icon displayed in the Terrain Tools overlay when the Terrain Tool isn't
selected.  
[OnIcon](TerrainTools.TerrainPaintToolWithOverlaysBase.OnIcon.html)| The icon
displayed in the Terrain Tools overlay when the terrain tool is selected.  
[Terrain](TerrainTools.TerrainPaintToolWithOverlaysBase.Terrain.html)| The
last hit terrain or the last active instance of a terrain object.  
  
### Public Methods

[GetDescription](TerrainTools.TerrainPaintToolWithOverlaysBase.GetDescription.html)|
Description of the Terrain Tool.  
---|---  
[GetName](TerrainTools.TerrainPaintToolWithOverlaysBase.GetName.html)| Name of
the Terrain Tool.  
[OnActivated](TerrainTools.TerrainPaintToolWithOverlaysBase.OnActivated.html)|
This function is called when the tool is activated.  
[OnDisable](TerrainTools.TerrainPaintToolWithOverlaysBase.OnDisable.html)|
Called when the tool is destroyed.  
[OnEnable](TerrainTools.TerrainPaintToolWithOverlaysBase.OnEnable.html)|
Called when the tool is created.  
[OnEnterToolMode](TerrainTools.TerrainPaintToolWithOverlaysBase.OnEnterToolMode.html)|
This function is called when the Terrain Tool is activated.  
[OnExitToolMode](TerrainTools.TerrainPaintToolWithOverlaysBase.OnExitToolMode.html)|
This function is called when the Terrain Tool becomes inactive.  
[OnInspectorGUI](TerrainTools.TerrainPaintToolWithOverlaysBase.OnInspectorGUI.html)|
Custom Terrain Tool OnInspectorGUI callback.  
[OnPaint](TerrainTools.TerrainPaintToolWithOverlaysBase.OnPaint.html)| Custom
Terrain Tool paint callback.  
[OnRenderBrushPreview](TerrainTools.TerrainPaintToolWithOverlaysBase.OnRenderBrushPreview.html)|
Use this method to implement custom tool preview and UI behavior that only
renders while the mouse is within the SceneView bounds or while you're
actively using this tool.  
[OnSceneGUI](TerrainTools.TerrainPaintToolWithOverlaysBase.OnSceneGUI.html)|
Custom Terrain Tool OnSceneGUI callback.  
[OnToolGUI](TerrainTools.TerrainPaintToolWithOverlaysBase.OnToolGUI.html)|
This method is used to implement the custom terrain editor paint tool.  
[OnToolSettingsGUI](TerrainTools.TerrainPaintToolWithOverlaysBase.OnToolSettingsGUI.html)|
Contains the IMGUI code for custom settings beyond the common settings.  
[OnWillBeDeactivated](TerrainTools.TerrainPaintToolWithOverlaysBase.OnWillBeDeactivated.html)|
Invoked before the terrain paint tool with overlays stops being the active
tool.  
  
### Inherited Members

### Properties

[gridSnapEnabled](EditorTools.EditorTool-gridSnapEnabled.html)| Use this
property to allow the current EditorTool to enable/disable grid snapping.  
---|---  
[target](EditorTools.EditorTool-target.html)| The object being inspected.  
[targets](EditorTools.EditorTool-targets.html)| An array of the objects being
inspected.  
[toolbarIcon](EditorTools.EditorTool-toolbarIcon.html)| The icon and tooltip
for this custom editor tool. If this function is not implemented, the toolbar
displays the Inspector icon for the target type. If no target type is defined,
the toolbar displays the Tool Mode icon.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[IsAvailable](EditorTools.EditorTool.IsAvailable.html)| Checks whether the
custom editor tool is available based on the state of the editor.  
---|---  
[PopulateMenu](EditorTools.EditorTool.PopulateMenu.html)| Adds menu items to
Scene view context menu.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
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

