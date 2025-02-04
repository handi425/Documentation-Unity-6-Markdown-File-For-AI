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

# TerrainPaintTool<T0>

class in UnityEditor.TerrainTools

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

Base class for terrain painting tools.

Derive from this class to implement your own terrain painting tools.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.TerrainTools;  
      
    namespace UnityEditor.TerrainTools
    {
        public class MyPaintHeightTool : TerrainPaintTool<MyPaintHeightTool>
        {
            [Material](Material.html) m_Material = null;
            [Material](Material.html) GetPaintMaterial()
            {
                if (m_Material == null)
                    m_Material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Hidden/[Terrain](Terrain.html)/PaintHeight"));
                return m_Material;
            }  
      
            public override string GetName()
            {
                return "My Paint Height [Tool](Tool.html)";
            }  
      
            public override string GetDescription()
            {
                return "Left click to raise.\n\nHold shift and left click to lower.";
            }  
      
            public override void OnRenderBrushPreview([Terrain](Terrain.html) terrain, [IOnSceneGUI](TerrainTools.IOnSceneGUI.html) editContext)
            {
                [TerrainPaintUtilityEditor.ShowDefaultPreviewBrush](TerrainTools.TerrainPaintUtilityEditor.ShowDefaultPreviewBrush.html)(terrain, editContext.brushTexture, editContext.brushSize);
            }  
      
            public override bool OnPaint([Terrain](Terrain.html) terrain, [IOnPaint](TerrainTools.IOnPaint.html) editContext)
            {
                [Material](Material.html) mat = [TerrainPaintUtility.GetBuiltinPaintMaterial](TerrainTools.TerrainPaintUtility.GetBuiltinPaintMaterial.html)();  
      
                float rotationDegrees = 0.0f;
                [BrushTransform](TerrainTools.BrushTransform.html) brushXform = [TerrainPaintUtility.CalculateBrushTransform](TerrainTools.TerrainPaintUtility.CalculateBrushTransform.html)(terrain, editContext.uv, editContext.brushSize, rotationDegrees);
                [PaintContext](TerrainTools.PaintContext.html) paintContext = [TerrainPaintUtility.BeginPaintHeightmap](TerrainTools.TerrainPaintUtility.BeginPaintHeightmap.html)(terrain, brushXform.GetBrushXYBounds());  
      
                // apply brush
                [Vector4](Vector4.html) brushParams = new [Vector4](Vector4.html)(editContext.brushStrength * 0.01f, 0.0f, 0.0f, 0.0f);
                mat.SetTexture("_BrushTex", editContext.brushTexture);
                mat.SetVector("_BrushParams", brushParams);
                [TerrainPaintUtility.SetupTerrainToolMaterialProperties](TerrainTools.TerrainPaintUtility.SetupTerrainToolMaterialProperties.html)(paintContext, brushXform, mat);  
      
                [Graphics.Blit](Graphics.Blit.html)(paintContext.sourceRenderTexture, paintContext.destinationRenderTexture, mat, (int)[TerrainBuiltinPaintMaterialPasses.RaiseLowerHeight](TerrainTools.TerrainBuiltinPaintMaterialPasses.RaiseLowerHeight.html));  
      
                [TerrainPaintUtility.EndPaintHeightmap](TerrainTools.TerrainPaintUtility.EndPaintHeightmap.html)(paintContext, "[Terrain](Terrain.html) Paint - MyPaintHeightTool");
                return false;
            }
        }
    }
    

### Public Methods

[GetDescription](TerrainTools.TerrainPaintTool_1.GetDescription.html)|
Retrieves the description of the custom terrain tool.  
---|---  
[GetName](TerrainTools.TerrainPaintTool_1.GetName.html)| Retrieves the name of
the custom terrain tool.  
[OnDisable](TerrainTools.TerrainPaintTool_1.OnDisable.html)| Called when the
tool is destroyed.  
[OnEnable](TerrainTools.TerrainPaintTool_1.OnEnable.html)| Called when the
tool is created.  
[OnEnterToolMode](TerrainTools.TerrainPaintTool_1.OnEnterToolMode.html)|
Called when the tool is activated.  
[OnExitToolMode](TerrainTools.TerrainPaintTool_1.OnExitToolMode.html)| Called
when the tool becomes inactive.  
[OnInspectorGUI](TerrainTools.TerrainPaintTool_1.OnInspectorGUI.html)| Custom
terrain tool OnInspectorGUI callback.  
[OnPaint](TerrainTools.TerrainPaintTool_1.OnPaint.html)| Custom terrain tool
paint callback.  
[OnRenderBrushPreview](TerrainTools.TerrainPaintTool_1.OnRenderBrushPreview.html)|
Use this method to implement custom tool preview and UI behavior that will
only render while the mouse is within the SceneView bounds or while you're
actively using this tool.  
[OnSceneGUI](TerrainTools.TerrainPaintTool_1.OnSceneGUI.html)| Custom terrain
tool OnSceneGUI callback.  
  
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

