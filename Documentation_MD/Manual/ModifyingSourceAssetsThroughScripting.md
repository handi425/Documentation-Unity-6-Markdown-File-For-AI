[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/ModifyingSourceAssetsThroughScripting.html)
  * [中文](/cn/current/Manual/ModifyingSourceAssetsThroughScripting.html)
  * [日本語](/ja/current/Manual/ModifyingSourceAssetsThroughScripting.html)
  * [한국어](/kr/current/Manual/ModifyingSourceAssetsThroughScripting.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/ModifyingSourceAssetsThroughScripting.html)
  * [中文](/cn/current/Manual/ModifyingSourceAssetsThroughScripting.html)
  * [日本語](/ja/current/Manual/ModifyingSourceAssetsThroughScripting.html)
  * [한국어](/kr/current/Manual/ModifyingSourceAssetsThroughScripting.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [Scripting with Assets](ScriptingAssets.html)
  * Modifying Source Assets Through Scripting

[](StreamingAssets.html)

Streaming Assets

[](AssetPackages.html)

Asset packages

# Modifying Source Assets Through Scripting

## Automatic Instantiation

Usually when you want to make a modification to any sort of game asset, you
want it to happen at runtime and you want it to be temporary. For example, if
your character picks up an invincibility power-up, you might want to change
the **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) of the **material** An asset that
defines how a surface should be rendered. [More info](class-Material.html)  
See in [Glossary](Glossary.html#Material) for the player character to visually
demonstrate the invincible state. This action involves modifying the material
that’s being used. This modification is not permanent because we don’t want
the material to have a different shader when we exit **Play Mode**.

However, it is possible in Unity to write **scripts** A piece of code that
allows you to create your own Components, trigger game events, modify
Component properties over time and respond to user input in any way you like.
[More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) that will permanently modify a source
asset. Let’s use the above material example as a starting point.

To temporarily change the material’s shader, we change the **shader** property
of the **material** component.

    
    
    private var invincibleShader = Shader.Find ("Specular");
    
    function StartInvincibility {
        renderer.material.shader = invincibleShader;
    }
    

When using this script and exiting Play Mode, the state of the
**[material](../ScriptReference/Material.html)** will be reset to whatever it
was before entering Play Mode initially. This happens because whenever
renderer.material is accessed, the material is automatically instantiated and
the instance is returned. This instance is simultaneously and automatically
applied to the renderer. So you can make any changes that your heart desires
without fear of permanence.

## Direct Modification

### IMPORTANT NOTE

The method presented below will modify actual source asset files used within
Unity. These modifications are not undoable. Use them with caution.

Now let’s say that we don’t want the material to reset when we exit play mode.
For this, you can use [renderer.sharedMaterial](../ScriptReference/Renderer-
sharedMaterial.html). The sharedMaterial property will return the actual asset
used by this renderer (and maybe others).

The code below will permanently change the material to use the Specular
shader. It will not reset the material to the state it was in before Play
Mode.

    
    
    private var invincibleShader = Shader.Find ("Specular");
    
    function StartInvincibility {
        renderer.sharedMaterial.shader = invincibleShader;
    }
    

As you can see, making any changes to a sharedMaterial can be both useful and
risky. Any change made to a sharedMaterial will be permanent, and not
undoable.

## Applicable Class Members

The same formula described above can be applied to more than just materials.
The full list of assets that follow this convention is as follows:

  * Materials: renderer.material and renderer.sharedMaterial
  * Meshes: meshFilter.**mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) and meshFilter.sharedMesh

  * **Physics Materials** A physics asset for adjusting the friction and bouncing effects of colliding objects. [More info](class-PhysicsMaterial.html)  
See in [Glossary](Glossary.html#PhysicsMaterial): **collider** An invisible
shape that is used to handle physical collisions for an object. A collider
doesn’t need to be exactly the same shape as the object’s mesh - a rough
approximation is often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider).material and collider.sharedMaterial

## Direct Assignment

If you declare a public variable of any above class: Material, Mesh, or
Physics Material, and make modifications to the asset using that variable
instead of using the relevant class member, you will not receive the benefits
of automatic instantiation before the modifications are applied.

## Assets that are not automatically instantiated

There are two different assets that are never automatically instantiated when
modifying them.

  * [Texture2D](../ScriptReference/Texture2D.html)
  * [TerrainData](../ScriptReference/TerrainData.html)

Any modifications made to these assets through scripting are always permanent,
and never undoable. So if you’re changing your **terrain** The landscape in
your scene. A Terrain GameObject adds a large flat plane to your scene and you
can use the Terrain’s Inspector window to create a detailed landscape. [More
info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain)’s **heightmap** A greyscale Texture
that stores height data for an object. Each pixel stores the height difference
perpendicular to the face that pixel represents.  
See in [Glossary](Glossary.html#Heightmap) through scripting, you’ll need to
account for instantiating and assigning values on your own. Same goes for
Textures. If you change the **pixels** The smallest unit in a computer image.
Pixel size depends on your screen resolution. Pixel lighting is calculated at
every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) of a texture file, the change is
permanent.

## iOS and Android Notes

[Texture2D](../ScriptReference/Texture2D.html) assets are never automatically
instantiated when modifying them in iOS and Android projects. Any
modifications made to these assets through scripting are always permanent, and
never undoable. So if you change the pixels of a texture file, the change is
permanent.

[](StreamingAssets.html)

Streaming Assets

[](AssetPackages.html)

Asset packages

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

