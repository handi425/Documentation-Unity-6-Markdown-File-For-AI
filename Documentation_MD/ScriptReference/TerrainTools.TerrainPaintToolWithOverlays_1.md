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

# TerrainPaintToolWithOverlays<T0>

class in UnityEditor.TerrainTools

/

Inherits
from:[TerrainTools.TerrainPaintToolWithOverlaysBase](TerrainTools.TerrainPaintToolWithOverlaysBase.html)

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

Base class for Terrain painting tools, which inherit from Editor Tools.

Derive from this class to implement your own terrain painting tools, which
also appear in the Terrain Tools overlay.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.TerrainTools;  
      
    class CustomTerrainToolWithOverlays : TerrainPaintToolWithOverlays<CustomTerrainToolWithOverlays>
    {
        private float m_BrushRotation;
        
        // Return true for this property to show the brush selector overlay
        public override bool HasBrushMask => true;  
      
        // Return true for this property to show the tool settings overlay
        public override bool HasToolSettings => true;
        
        // Return true for this property to display the brush attributes overlay
        public override bool HasBrushAttributes => true;
        
        // [File](Windows.File.html) names of the light theme icons - prepending d_ to the file name generates dark theme variants.
        // public override string OnIcon => "Assets/Icon_on.png";
        // public override string OffIcon => "Assets/Icon_off.png";  
      
        // The toolbar category the icon appears under
         public override [TerrainCategory](TerrainTools.TerrainCategory.html) [Category](Unity.Android.Gradle.Manifest.Category.html) => [TerrainCategory.CustomBrushes](TerrainTools.TerrainCategory.CustomBrushes.html);  
      
        // Where in the icon list the icon appears
        public override int IconIndex => 100;
        
        // Name of the [Terrain](Terrain.html) [Tool](Tool.html). This appears in the tool UI
        public override string GetName()
        {
            return "Examples/Basic Custom [Terrain](Terrain.html) [Tool](Tool.html)";
        }  
      
        // Description for the [Terrain](Terrain.html) [Tool](Tool.html). This appears in the tool UI
        public override string GetDescription()
        {
            return "This [Terrain](Terrain.html) [Tool](Tool.html) shows how to add custom UI to a tool and paint height.";
        }  
      
        // Override this function to add UI elements to the inspector
        public override void OnInspectorGUI([Terrain](Terrain.html) terrain, [IOnInspectorGUI](TerrainTools.IOnInspectorGUI.html) editContext)
        {
            [EditorGUILayout.HelpBox](EditorGUILayout.HelpBox.html)("In [Terrain](Terrain.html) Inspector", [MessageType.None](MessageType.None.html)); 
            editContext.ShowBrushesGUI(5, [BrushGUIEditFlags.All](TerrainTools.BrushGUIEditFlags.All.html));
            m_BrushRotation = [EditorGUILayout.Slider](EditorGUILayout.Slider.html)("Rotation", m_BrushRotation, 0, 360);
        }  
      
        // Override this function to add UI elements to the tool settings overlay 
        public override void OnToolSettingsGUI([Terrain](Terrain.html) terrain, [IOnInspectorGUI](TerrainTools.IOnInspectorGUI.html) editContext)
        {
            [EditorGUILayout.HelpBox](EditorGUILayout.HelpBox.html)("In Overlays", [MessageType.None](MessageType.None.html)); 
            m_BrushRotation = [EditorGUILayout.Slider](EditorGUILayout.Slider.html)("Rotation", m_BrushRotation, 0, 360);
        }  
      
        // Ease of use function for rendering modified [Terrain](Terrain.html) [Texture](Texture.html) data into a [PaintContext](TerrainTools.PaintContext.html). Both OnRenderBrushPreview and OnPaint use this.
        private void RenderIntoPaintContext(UnityEngine.TerrainTools.PaintContext paintContext, [Texture](Texture.html) brushTexture, float brushOpacity, UnityEngine.TerrainTools.BrushTransform brushXform)
        {
            // Get the built-in painting [Material](Material.html) reference
            [Material](Material.html) mat = UnityEngine.TerrainTools.TerrainPaintUtility.GetBuiltinPaintMaterial();
            // Bind the current brush texture
            mat.SetTexture("_BrushTex", brushTexture);
            // Bind the tool-specific shader properties
            var opacity = Event.current.control ? -brushOpacity : brushOpacity;
            mat.SetVector("_BrushParams", new [Vector4](Vector4.html)(opacity, 0.0f, 0.0f, 0.0f));
            // Set up the material for reading from/writing into the [PaintContext](TerrainTools.PaintContext.html) texture data. This step is necessary to set up the correct shader properties for appropriately transforming UVs and sampling textures within the shader
            UnityEngine.TerrainTools.TerrainPaintUtility.SetupTerrainToolMaterialProperties(paintContext, brushXform, mat);
            // Render into the [PaintContext](TerrainTools.PaintContext.html)'s destinationRenderTexture using the built-in painting [Material](Material.html). The ID for the Raise/Lower pass is 0
            [Graphics.Blit](Graphics.Blit.html)(paintContext.sourceRenderTexture, paintContext.destinationRenderTexture, mat, 0);
        }
        
        // Render [Tool](Tool.html) previews in the [Scene](SceneManagement.Scene.html) view
        public override void OnRenderBrushPreview([Terrain](Terrain.html) terrain, [IOnSceneGUI](TerrainTools.IOnSceneGUI.html) editContext)
        {
            // Don't render preview if this isn't a Repaint
            if (Event.current.type != [EventType.Repaint](EventType.Repaint.html)) return;  
      
            // Only do the rest if user mouse hits valid terrain
            if (!editContext.hitValidTerrain) return;  
      
            // Get the current [BrushTransform](TerrainTools.BrushTransform.html) under the mouse position relative to the [Terrain](Terrain.html)
            UnityEngine.TerrainTools.BrushTransform brushXform = UnityEngine.TerrainTools.TerrainPaintUtility.CalculateBrushTransform(terrain, editContext.raycastHit.textureCoord, editContext.brushSize, m_BrushRotation);
            // Get the [PaintContext](TerrainTools.PaintContext.html) for the current [BrushTransform](TerrainTools.BrushTransform.html). This has a sourceRenderTexture from which to read existing [Terrain](Terrain.html) texture data.
            UnityEngine.TerrainTools.PaintContext paintContext = UnityEngine.TerrainTools.TerrainPaintUtility.BeginPaintHeightmap(terrain, brushXform.GetBrushXYBounds(), 1);
            // Get the built-in [Material](Material.html) for rendering Brush Previews
            [Material](Material.html) previewMaterial = [TerrainPaintUtilityEditor.GetDefaultBrushPreviewMaterial](TerrainTools.TerrainPaintUtilityEditor.GetDefaultBrushPreviewMaterial.html)();
            // Render the brush preview for the sourceRenderTexture. This shows up as a projected brush mesh rendered on top of the [Terrain](Terrain.html)
            [TerrainPaintUtilityEditor.DrawBrushPreview](TerrainTools.TerrainPaintUtilityEditor.DrawBrushPreview.html)(paintContext, [TerrainBrushPreviewMode.SourceRenderTexture](TerrainTools.TerrainBrushPreviewMode.SourceRenderTexture.html), editContext.brushTexture, brushXform, previewMaterial, 0);
            // Render changes into the [PaintContext](TerrainTools.PaintContext.html) destinationRenderTexture
            RenderIntoPaintContext(paintContext, editContext.brushTexture, editContext.brushStrength, brushXform);
            // Restore old render target
            [RenderTexture.active](RenderTexture-active.html) = paintContext.oldRenderTexture;
            // Bind the sourceRenderTexture to the preview [Material](Material.html). This is used to compute deltas in height
            previewMaterial.SetTexture("_HeightmapOrig", paintContext.sourceRenderTexture);
            // Render a procedural mesh displaying the delta/displacement in height from the source [Terrain](Terrain.html) texture data. When you modify [Terrain](Terrain.html) height, this shows how much the next paint operation alters the [Terrain](Terrain.html) height
            [TerrainPaintUtilityEditor.DrawBrushPreview](TerrainTools.TerrainPaintUtilityEditor.DrawBrushPreview.html)(paintContext, [TerrainBrushPreviewMode.DestinationRenderTexture](TerrainTools.TerrainBrushPreviewMode.DestinationRenderTexture.html), editContext.brushTexture, brushXform, previewMaterial, 1);
            // Cleanup resources
            UnityEngine.TerrainTools.TerrainPaintUtility.ReleaseContextResources(paintContext);
        }
        
        // Perform painting operations that modify the [Terrain](Terrain.html) texture data
        public override bool OnPaint([Terrain](Terrain.html) terrain, [IOnPaint](TerrainTools.IOnPaint.html) editContext)
        {
            // Get the current [BrushTransform](TerrainTools.BrushTransform.html) under the mouse position relative to the [Terrain](Terrain.html)
            UnityEngine.TerrainTools.BrushTransform brushXform = UnityEngine.TerrainTools.TerrainPaintUtility.CalculateBrushTransform(terrain, editContext.uv, editContext.brushSize, m_BrushRotation);
            // Get the [PaintContext](TerrainTools.PaintContext.html) for the current [BrushTransform](TerrainTools.BrushTransform.html). This has a sourceRenderTexture from which to read existing [Terrain](Terrain.html) texture data
            // and a destinationRenderTexture into which to write new [Terrain](Terrain.html) texture data
            UnityEngine.TerrainTools.PaintContext paintContext = UnityEngine.TerrainTools.TerrainPaintUtility.BeginPaintHeightmap(terrain, brushXform.GetBrushXYBounds());
            // Call the common rendering function that OnRenderBrushPreview and OnPaint use
            RenderIntoPaintContext(paintContext, editContext.brushTexture, editContext.brushStrength, brushXform);
            // Commit the modified [PaintContext](TerrainTools.PaintContext.html) with a provided string for tracking [Undo](Undo.html) operations. This function handles [Undo](Undo.html) and resource cleanup for you
            UnityEngine.TerrainTools.TerrainPaintUtility.EndPaintHeightmap(paintContext, "[Terrain](Terrain.html) Paint - Raise or Lower Height");  
      
            // Return whether Trees and Details should be hidden while you paint with this [Terrain](Terrain.html) [Tool](Tool.html)
            return true;
        }
    }
    

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
[Category](TerrainTools.TerrainPaintToolWithOverlaysBase.Category.html)| The
TerrainCategory that the Terrain Tool belongs to.  
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

[IsAvailable](EditorTools.EditorTool.IsAvailable.html)| Checks whether the
custom editor tool is available based on the state of the editor.  
---|---  
[OnActivated](EditorTools.EditorTool.OnActivated.html)| Invoked after this
EditorTool becomes the active tool.  
[OnToolGUI](EditorTools.EditorTool.OnToolGUI.html)| Use this method to
implement a custom editor tool.  
[OnWillBeDeactivated](EditorTools.EditorTool.OnWillBeDeactivated.html)|
Invoked before this EditorTool stops being the active tool.  
[PopulateMenu](EditorTools.EditorTool.PopulateMenu.html)| Adds menu items to
Scene view context menu.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
[ToString](Object.ToString.html)| Returns the name of the object.  
[GetDescription](TerrainTools.TerrainPaintToolWithOverlaysBase.GetDescription.html)|
Description of the Terrain Tool.  
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

