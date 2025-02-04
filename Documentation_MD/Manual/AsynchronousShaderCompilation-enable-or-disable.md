[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/AsynchronousShaderCompilation-enable-or-disable.html)
  * [中文](/cn/current/Manual/AsynchronousShaderCompilation-enable-or-disable.html)
  * [日本語](/ja/current/Manual/AsynchronousShaderCompilation-enable-or-disable.html)
  * [한국어](/kr/current/Manual/AsynchronousShaderCompilation-enable-or-disable.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/AsynchronousShaderCompilation-enable-or-disable.html)
  * [中文](/cn/current/Manual/AsynchronousShaderCompilation-enable-or-disable.html)
  * [日本語](/ja/current/Manual/AsynchronousShaderCompilation-enable-or-disable.html)
  * [한국어](/kr/current/Manual/AsynchronousShaderCompilation-enable-or-disable.html)

  * [Materials and shaders](materials-and-shaders.html)
  * [Shaders](Shaders.html)
  * [Troubleshooting shaders](shader-troubleshooting.html)
  * [Fixing hitches or stalls](shader-reduce-stalling.html)
  * [Asynchronous shader compilation in the Editor](AsynchronousShaderCompilation.html)
  * Enable or disable asynchronous shader compilation

[](AsynchronousShaderCompilation-introduction.html)

Introduction to asynchronous shader compilation

[](AsynchronousShaderCompilation-detect.html)

Detect asynchronous shader compilation

# Enable or disable asynchronous shader compilation

Asynchronous **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) compilation is enabled by default.

To enable or disable asynchronous shader compilation:

  1. Go to **Edit > Project Settings > Editor**.
  2. At the bottom of the Editor settings, under **Shader Compilation** , check or uncheck the **Asynchronous Shader Compilation** checkbox.

**Note:** Enabling and disabling asynchronous shader compilation in this way
affects only the **Scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and Game views by default. If you want
to use it in other parts of the Editor, see Custom Editor tools and
asynchronous shader compilation.

## Enable or disable asynchronous shader compilation for specific rendering
calls

You can enable or disable asynchronous shader compilation for specific
rendering commands in your C# **scripts** A piece of code that allows you to
create your own Components, trigger game events, modify Component properties
over time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts).

The following instructions show you how to enable or disable the feature in an
immediate scope, and a
[CommandBuffer](../ScriptReference/Rendering.CommandBuffer.html) scope.

#### In an immediate scope

In an immediate scope, you can use
[`ShaderUtil.allowAsyncCompilation`](../ScriptReference/ShaderUtil-
allowAsyncCompilation.html).

To do this:

  1. Store the current state of `ShaderUtil.allowAsyncCompilation` in a variable.
  2. Before you call the rendering commands, set `ShaderUtil.allowAsyncCompilation` to `false`.
  3. Call the rendering commands.
  4. After calling the rendering commands, restore `ShaderUtil.allowAsyncCompilation` back to its previous state.

Here is a pseudo-code example:

    
    
    // Store the current state
    bool oldState = ShaderUtil.allowAsyncCompilation;
    
    // Disable async compilation
    ShaderUtil.allowAsyncCompilation = false;
    
    // Enter your rendering code that should never use the placeholder shader, for example UI elements or characters.
    Graphics.RenderMesh(...);
    
    // Restore the old state
    ShaderUtil.allowAsyncCompilation = oldState;
    

#### In a CommandBuffer scope

In a `CommandBuffer` scope, you can use
[`ShaderUtil.SetAsyncCompilation`](../ScriptReference/ShaderUtil.SetAsyncCompilation.html)
and
[`ShaderUtil.RestoreAsyncCompilation`](../ScriptReference/ShaderUtil.RestoreAsyncCompilation.html).

  1. Immediately before you call the rendering commands, call `ShaderUtil.SetAsyncCompilation`, and set it to `false`. Subsequent commands in the CommandBuffer won’t allow asynchronous compilation.
  2. Add the rendering commands to the CommandBuffer.
  3. After the rendering commands, call [`Shader.Util.RestoreAsyncCompilation`](../ScriptReference/ShaderUtil.RestoreAsyncCompilation.html) to restore the state of asynchronous shader compilation.

Here is an example:

    
    
    // Create the CommandBuffer
    CommandBuffer cmd = new CommandBuffer();
    
    // Disable async compilation for subsequent commands
    ShaderUtil.SetAsyncCompilation(cmd, false);
    
    /// Enter your rendering commands that should never use the placeholder shader, for example UI elements or characters.
    cmd.DrawMesh(...);
    
    // Restore the old state
    ShaderUtil.RestoreAsyncCompilation(cmd);
    

## Disable asynchronous compilation for specific Shader objects

You can disable asynchronous shader compilation for specific **Shader
objects** An instance of the Shader class, a Shader object is container for
shader programs and GPU instructions, and information that tells Unity how to
use them. Use them with materials to determine the appearance of your scene.
[More info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject) by forcing the Editor to always
compile them synchronously. This is a good option for data generating Shader
objects that are always present at the start of your rendering, and which are
relatively quick to compile. You would most likely need this if you are
performing [advanced rendering](AsynchronousShaderCompilation-avoid-cyan-
placeholder-shaders.html).

To force synchronous compilation for a Shader object, add the `#pragma
editor_sync_compilation` [directive](writing-shader-writing-shader-programs-
hlsl.html) to your shader source code.

**Note:** You should not force synchronous compilation for complex Shader
objects that encounter new shader variants during rendering; this can stall
rendering in the Editor.

## Custom Editor tools and asynchronous shader compilation

By default, asynchronous Shader compilation works in the Game and **Scene
views** An interactive view into the world you are creating. You use the Scene
View to select and position scenery, characters, cameras, lights, and all
other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView). If you want to use it in custom
Editor tools, you can enable it via C# for your custom tool.

To do this, you can enable asynchronous shader compilation for specific
rendering calls.

[](AsynchronousShaderCompilation-introduction.html)

Introduction to asynchronous shader compilation

[](AsynchronousShaderCompilation-detect.html)

Detect asynchronous shader compilation

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

