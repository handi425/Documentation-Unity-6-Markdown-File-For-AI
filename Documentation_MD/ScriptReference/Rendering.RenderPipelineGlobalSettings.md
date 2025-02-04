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

# RenderPipelineGlobalSettings

class in UnityEngine.Rendering

/

Inherits from:[ScriptableObject](ScriptableObject.html)

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

Leave feedback

  

Implements
interfaces:[ISerializationCallbackReceiver](ISerializationCallbackReceiver.html)

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

A [ScriptableObject](ScriptableObject.html) to associate with a
[RenderPipeline](Rendering.RenderPipeline.html) and store project-wide
settings for that Pipeline.

A single RenderPipelineGlobalSettings instance can be registered to the
GraphicsSettings via GraphicsSettings.RegisterRenderPipelineSettings. We
recommend to use this ScriptableObject to save RenderPipeline settings you
would find in the GraphicsSettings.

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;  
      
    using UnityEngine;
    using UnityEngine.Rendering;  
      
    #if UNITY_EDITOR
    using UnityEditor.Rendering;
    #endif  
      
    public class ExampleRenderPipelineAsset : [RenderPipelineAsset](Rendering.RenderPipelineAsset.html)
    {
        protected override [RenderPipeline](Rendering.RenderPipeline.html) CreatePipeline()
        {
            return new ExampleRenderPipeline();
        }
    }  
      
    public class ExampleRenderPipeline : [RenderPipeline](Rendering.RenderPipeline.html)
    {
        public virtual [RenderPipelineGlobalSettings](Rendering.RenderPipelineGlobalSettings.html) globalSettings => ExampleRPGlobalSettings.instance;  
      
        protected override void Render([ScriptableRenderContext](Rendering.ScriptableRenderContext.html) renderContext, [Camera](Camera.html)[] cameras)
        {
    #if UNITY_EDITOR
    	// On [Editor](Editor.html) we must make sure the Global [Settings](Rendering.RayTracingAccelerationStructure.Settings.html) [Asset](VersionControl.Asset.html) is registered into the [GraphicsSettings](Rendering.GraphicsSettings.html)
    	// [Graphics](Graphics.html) [Settings](Rendering.RayTracingAccelerationStructure.Settings.html) will make sure the asset is available on player builds
            	if (globalSettings == null)
    	{
     	       var mySettings = ExampleRPGlobalSettings.Create();
     	       ExampleRPGlobalSettings.RegisterToGraphicsSettings(mySettings);
    	}
    #endif  
      
            // Do something
        }
    }  
      
    [SupportedOnRenderPipeline(typeof(ExampleRenderPipelineAsset))]
    public class ExampleRPGlobalSettings : [RenderPipelineGlobalSettings](Rendering.RenderPipelineGlobalSettings.html)
    {
        private static ExampleRPGlobalSettings cachedInstance = null;
        public static ExampleRPGlobalSettings instance
        {
            get
            {
                if (cachedInstance == null)
                    cachedInstance = [GraphicsSettings.GetSettingsForRenderPipeline](Rendering.GraphicsSettings.GetSettingsForRenderPipeline.html)<ExampleRenderPipeline>() as ExampleRPGlobalSettings;
                return cachedInstance;
            }
        }  
      
        /*   Use this pattern if you want to enable your global settings to use [IRenderPipelineGraphicsSettings](Rendering.IRenderPipelineGraphicsSettings.html)  
      
    	[[SerializeReference](SerializeReference.html)] private List<[IRenderPipelineGraphicsSettings](Rendering.IRenderPipelineGraphicsSettings.html)> m_SettingsList = new();
     	protected override List<[IRenderPipelineGraphicsSettings](Rendering.IRenderPipelineGraphicsSettings.html)> settingsList => m_Settings;  
      
        */  
      
    #if UNITY_EDITOR
        public static void RegisterToGraphicsSettings(ExampleRPGlobalSettings newSettings)
        {
            [EditorGraphicsSettings.SetRenderPipelineGlobalSettingsAsset](Rendering.EditorGraphicsSettings.SetRenderPipelineGlobalSettingsAsset.html)<ExampleRenderPipeline>(newSettings as [RenderPipelineGlobalSettings](Rendering.RenderPipelineGlobalSettings.html));
            cachedInstance = null;
        }  
      
        public static void UnregisterToGraphicsSettings()
        {
            [EditorGraphicsSettings.SetRenderPipelineGlobalSettingsAsset](Rendering.EditorGraphicsSettings.SetRenderPipelineGlobalSettingsAsset.html)<ExampleRenderPipeline>(null);
            cachedInstance = null;
        }  
      
        static public ExampleRPGlobalSettings Create()
        {
            ExampleRPGlobalSettings assetCreated = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<ExampleRPGlobalSettings>();
            return assetCreated;
        }
    #endif
    }
    

### Properties

[settingsList](Rendering.RenderPipelineGlobalSettings-settingsList.html)|
Exposes a List<IRenderPipelineGraphicsSettings> that this
RenderPipelineGlobalSettings instance is managing.  
---|---  
  
### Public Methods

[Initialize](Rendering.RenderPipelineGlobalSettings.Initialize.html)| Editor-
only function that initializes the RenderPipelineGlobalSettings.  
---|---  
  
### Protected Methods

[Add](Rendering.RenderPipelineGlobalSettings.Add.html)| Adds a
IRenderPipelineGraphicsSettings interface to this instance of the
RenderPipelineGlobalSettings asset.  
---|---  
[Contains](Rendering.RenderPipelineGlobalSettings.Contains.html)| If the given
ISRPGraphicsSetting type is present in this RenderPipelineGlobalSettings
instance.  
[GetSettingsImplementingInterface](Rendering.RenderPipelineGlobalSettings.GetSettingsImplementingInterface.html)|
Get all settings for the currently active pipeline that implement
TSettingsInterfaceType.  
[Remove](Rendering.RenderPipelineGlobalSettings.Remove.html)| Removes a
IRenderPipelineGraphicsSettings interface from this instance of the
RenderPipelineGlobalSettings asset.  
[TryGet](Rendering.RenderPipelineGlobalSettings.TryGet.html)| Looks for a
IRenderPipelineGraphicsSettings interface in this instance of the
RenderPipelineGlobalSettings asset and returns true if it's found.  
[TryGetFirstSettingsImplementingInterface](Rendering.RenderPipelineGlobalSettings.TryGetFirstSettingsImplementingInterface.html)|
Try to get the first settings that implements TSettingsInterfaceType.  
  
### Inherited Members

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

