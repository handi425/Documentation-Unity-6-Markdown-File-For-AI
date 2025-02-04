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

# Light

class in UnityEngine

/

Inherits from:[Behaviour](Behaviour.html)

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

[Switch to Manual](../Manual/class-Light.html "Go to Light Component in the
Manual")

### Description

Script interface for [light components](../Manual/class-Light.html).

Use this to control all aspects of Unity's lights. The properties are an exact
match for the values shown in the Inspector.  
  
Usually lights are just created in the editor but sometimes you want to create
a light from a script:

    
    
    using UnityEngine;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Make a game object
            [GameObject](GameObject.html) lightGameObject = new [GameObject](GameObject.html)("The [Light](Light.html)");  
      
            // Add the light component
            [Light](Light.html) lightComp = lightGameObject.AddComponent<[Light](Light.html)>();  
      
            // Set color and position
            lightComp.color = [Color.blue](Color-blue.html);  
      
            // Set the position (or any transform property)
            lightGameObject.transform.position = new [Vector3](Vector3.html)(0, 5, 0);
        }
    }
    

### Properties

[areaSize](Light-areaSize.html)| The size of the area light.  
---|---  
[bakingOutput](Light-bakingOutput.html)| This property describes the output of
the last Global Illumination bake.  
[bounceIntensity](Light-bounceIntensity.html)| The multiplier that defines the
strength of the bounce lighting.  
[boundingSphereOverride](Light-boundingSphereOverride.html)| Bounding sphere
used to override the regular light bounding sphere during culling.  
[color](Light-color.html)| The color of the light.  
[colorTemperature](Light-colorTemperature.html)|  The color temperature of the
light. Correlated Color Temperature (abbreviated as CCT) is multiplied with
the color filter when calculating the final color of a light source. The color
temperature of the electromagnetic radiation emitted from an ideal black body
is defined as its surface temperature in Kelvin. White is 6500K according to
the D65 standard. A candle light is 1800K and a soft warm light bulb is 2700K.
If you want to use colorTemperature, GraphicsSettings.lightsUseLinearIntensity
and Light.useColorTemperature has to be enabled. Additional resources:
GraphicsSettings.lightsUseLinearIntensity,
GraphicsSettings.useColorTemperature.  
[commandBufferCount](Light-commandBufferCount.html)| Number of command buffers
set up on this light (Read Only).  
[cookie](Light-cookie.html)| The cookie texture projected by the light.  
[cookieSize](Light-cookieSize.html)| The size of a directional light's cookie.  
[cullingMask](Light-cullingMask.html)| This is used to light certain objects
in the Scene selectively.  
[dilatedRange](Light-dilatedRange.html)|  The Light.range property describes
the range of each point on the light. However, area lights consist of several
light-emitting points, and so the effective range is a bit larger, and depends
on the size of the area light. This property returns this larger range. Use
this property to find whether a given world-space point will be lit by the
area light. If not an area light, then returns the same value as Light.range.  
[enableSpotReflector](Light-enableSpotReflector.html)| Wether a Spot Light
should simulate having a reflector.  
[flare](Light-flare.html)| The flare asset to use for this light.  
[forceVisible](Light-forceVisible.html)| Force a light to be visible even if
outside the view frustum.  
[innerSpotAngle](Light-innerSpotAngle.html)| The angle of the spot light's
inner cone in degrees.  
[intensity](Light-intensity.html)| The Intensity of a light is multiplied with
the Light color.  
[layerShadowCullDistances](Light-layerShadowCullDistances.html)| Per-light,
per-layer shadow culling distances. Directional lights only.  
[lightmapBakeType](Light-lightmapBakeType.html)| This property describes what
part of a light's contribution can be baked (Editor only).  
[lightShadowCasterMode](Light-lightShadowCasterMode.html)| Allows you to
override the global Shadowmask Mode per light. Only use this with render
pipelines that can handle per light Shadowmask modes. Incompatible with the
legacy renderers.  
[lightUnit](Light-lightUnit.html)| The unit Light.intensity should be
displayed in.  
[luxAtDistance](Light-luxAtDistance.html)| How far away to measure
LightUnit.Lux from.  
[range](Light-range.html)|  The range of each point of the light. Since area
lights have a light emitting surface instead of a single point, the cumulative
range of the light is larger than this property. This larger range can be read
from the Light.dilatedRange property. For non-area lights, Light.range and
Light.dilatedRange return the same value.  
[renderingLayerMask](Light-renderingLayerMask.html)| Determines which
rendering LayerMask this Light affects.  
[renderMode](Light-renderMode.html)| How to render the light.  
[shadowAngle](Light-shadowAngle.html)| Controls the amount of artificial
softening applied to the edges of shadows cast by directional lights (Editor
only).  
[shadowBias](Light-shadowBias.html)| Shadow mapping constant bias.  
[shadowCustomResolution](Light-shadowCustomResolution.html)| The custom
resolution of the shadow map.  
[shadowMatrixOverride](Light-shadowMatrixOverride.html)| Matrix that overrides
the regular light projection matrix during shadow culling. Unity uses this
matrix if you set Light.useShadowMatrixOverride to true.  
[shadowNearPlane](Light-shadowNearPlane.html)| Near plane value to use for
shadow frustums.  
[shadowNormalBias](Light-shadowNormalBias.html)| Shadow mapping normal-based
bias.  
[shadowRadius](Light-shadowRadius.html)| Controls the amount of artificial
softening applied to the edges of shadows cast by the Point or Spot light
(Editor only).  
[shadowResolution](Light-shadowResolution.html)| The resolution of the shadow
map.  
[shadows](Light-shadows.html)| How this light casts shadows  
[shadowStrength](Light-shadowStrength.html)| Strength of light's shadows.  
[spotAngle](Light-spotAngle.html)| The angle of the spot light's cone in
degrees.  
[type](Light-type.html)| The type of the light.  
[useBoundingSphereOverride](Light-useBoundingSphereOverride.html)| Set to true
to override light bounding sphere for culling.  
[useColorTemperature](Light-useColorTemperature.html)| Set to true to use the
color temperature.  
[useShadowMatrixOverride](Light-useShadowMatrixOverride.html)| Set to true to
enable custom matrix for culling during shadows.  
[useViewFrustumForShadowCasterCull](Light-
useViewFrustumForShadowCasterCull.html)| Whether to cull shadows for this
Light when the Light is outside of the view frustum.  
  
### Public Methods

[AddCommandBuffer](Light.AddCommandBuffer.html)| Add a command buffer to be
executed at a specified place.  
---|---  
[AddCommandBufferAsync](Light.AddCommandBufferAsync.html)| Adds a command
buffer to the GPU's async compute queues and executes that command buffer when
graphics processing reaches a given point.  
[GetCommandBuffers](Light.GetCommandBuffers.html)| Get command buffers to be
executed at a specified place.  
[RemoveAllCommandBuffers](Light.RemoveAllCommandBuffers.html)| Remove all
command buffers set on this light.  
[RemoveCommandBuffer](Light.RemoveCommandBuffer.html)| Remove command buffer
from execution at a specified place.  
[RemoveCommandBuffers](Light.RemoveCommandBuffers.html)| Remove command
buffers from execution at a specified place.  
[Reset](Light.Reset.html)| Revert all light parameters to default.  
[SetLightDirty](Light.SetLightDirty.html)| Sets a light dirty to notify the
light baking backends to update their internal light representation (Editor
only).  
  
### Inherited Members

### Properties

[enabled](Behaviour-enabled.html)| Enabled Behaviours are Updated, disabled
Behaviours are not.  
---|---  
[isActiveAndEnabled](Behaviour-isActiveAndEnabled.html)| Reports whether a
GameObject and its associated Behaviour is active and enabled.  
[gameObject](Component-gameObject.html)| The game object this component is
attached to. A component is always attached to a game object.  
[tag](Component-tag.html)| The tag of this game object.  
[transform](Component-transform.html)| The Transform attached to this
GameObject.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[BroadcastMessage](Component.BroadcastMessage.html)| Calls the method named
methodName on every MonoBehaviour in this game object or any of its children.  
---|---  
[CompareTag](Component.CompareTag.html)| Checks the GameObject's tag against
the defined tag.  
[GetComponent](Component.GetComponent.html)| Gets a reference to a component
of type T on the same GameObject as the component specified.  
[GetComponentInChildren](Component.GetComponentInChildren.html)| Gets a
reference to a component of type T on the same GameObject as the component
specified, or any child of the GameObject.  
[GetComponentIndex](Component.GetComponentIndex.html)| Gets the index of the
component on its parent GameObject.  
[GetComponentInParent](Component.GetComponentInParent.html)| Gets a reference
to a component of type T on the same GameObject as the component specified, or
any parent of the GameObject.  
[GetComponents](Component.GetComponents.html)| Gets references to all
components of type T on the same GameObject as the component specified.  
[GetComponentsInChildren](Component.GetComponentsInChildren.html)| Gets
references to all components of type T on the same GameObject as the component
specified, and any child of the GameObject.  
[GetComponentsInParent](Component.GetComponentsInParent.html)| Gets references
to all components of type T on the same GameObject as the component specified,
and any parent of the GameObject.  
[SendMessage](Component.SendMessage.html)| Calls the method named methodName
on every MonoBehaviour in this game object.  
[SendMessageUpwards](Component.SendMessageUpwards.html)| Calls the method
named methodName on every MonoBehaviour in this game object and on every
ancestor of the behaviour.  
[TryGetComponent](Component.TryGetComponent.html)| Gets the component of the
specified type, if it exists.  
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
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

