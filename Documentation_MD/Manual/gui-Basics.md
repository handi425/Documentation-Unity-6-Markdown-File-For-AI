[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/gui-Basics.html)
  * [中文](/cn/current/Manual/gui-Basics.html)
  * [日本語](/ja/current/Manual/gui-Basics.html)
  * [한국어](/kr/current/Manual/gui-Basics.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/gui-Basics.html)
  * [中文](/cn/current/Manual/gui-Basics.html)
  * [日本語](/ja/current/Manual/gui-Basics.html)
  * [한국어](/kr/current/Manual/gui-Basics.html)

  * [Working in Unity](working-in-unity.html)
  * [User interface (UI)](UIToolkits.html)
  * [Immediate Mode GUI (IMGUI)](GUIScriptingGuide.html)
  * IMGUI Basics

[](GUIScriptingGuide.html)

Immediate Mode GUI (IMGUI)

[](gui-Controls.html)

IMGUI Controls

# IMGUI Basics

This section will explain the bare necessities for scripting **Controls** with
Unity’s Immediate Mode GUI system (IMGUI).

## Making Controls with IMGUI

Unity’s IMGUI controls make use of a special function called **OnGUI()**. The
**OnGUI()** function gets called every frame as long as the containing script
is enabled - just like the **Update()** function.

IMGUI controls themselves are very simple in structure. This structure is
evident in the following example.

    
    
    /* Example level loader */
    using UnityEngine;
    using System.Collections;
    
    public class GUITest : MonoBehaviour {
                
        void OnGUI ()
        {
            // Make a background box
            GUI.Box(new Rect(10,10,100,90), "Loader Menu");
        
            // Make the first button. If it is pressed, Application.Loadlevel (1) will be executed
            if(GUI.Button(new Rect(20,40,80,20), "Level 1"))
            {
                Application.LoadLevel(1);
            }
        
            // Make the second button.
            if(GUI.Button(new Rect(20,70,80,20), "Level 2")) 
            {
                Application.LoadLevel(2);
            }
        }
    }
    

This example is a complete, functional level loader. If you copy/paste this
script and attach it a **GameObject** The fundamental object in Unity scenes,
which can represent characters, props, scenery, cameras, waypoints, and more.
A GameObject’s functionality is defined by the Components attached to it.
[More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), you’ll see the following menu
appear in when you enter **Play Mode** :

![The Loader Menu created by the example code](../uploads/Main/guiScripting-
BasicsLoaderMenuExample.png) The Loader Menu created by the example code

Let’s take a look at the details of the example code:

The first GUI line, **GUI.Box (Rect (10,10,100,90), “Loader Menu”);** displays
a **Box** Control with the header text “Loader Menu”. It follows the typical
GUI Control declaration scheme which we’ll explore momentarily.

The next GUI line is a **Button** Control declaration. Notice that it is
slightly different from the Box Control declaration. Specifically, the entire
Button declaration is placed inside an **if** statement. When the game is
running and the Button is clicked, this **if** statement returns true and any
code inside the **if** block is executed.

Since the **OnGUI()** code gets called every frame, you don’t need to
explicitly create or destroy GUI controls. The line that declares the Control
is the same one that creates it. If you need to display Controls at specific
times, you can use any kind of scripting logic to do so.

    
    
    /* Flashing button example */
    using UnityEngine;
    using System.Collections;
    
    public class GUITest : MonoBehaviour
    {
                
        void OnGUI () 
        {
            if (Time.time % 2 < 1) 
            {
                if (GUI.Button (new Rect (10,10,200,20), "Meet the flashing button"))
                {
                    print ("You clicked me!");
                }
            }
        }
    }
    

Here, **GUI.Button()** only gets called every other second, so the button will
appear and disappear. Naturally, the user can only click it when the button is
visible.

As you can see, you can use any desired logic to control when GUI Controls are
displayed and functional. Now we will explore the details of each Control’s
declaration.

## Anatomy of a Control

There are three key pieces of information required when declaring a GUI
Control:

**Type** (**Position** , **Content**)

Observe that this structure is a function with two arguments. We’ll explore
the details of this structure now.

### Type

**Type** is the **Control Type** , and is declared by calling a function in
Unity’s [GUI class](../ScriptReference/GUI.html) or the [GUILayout
class](../ScriptReference/GUILayout.html), which is discussed at length in the
[Layout Modes](gui-Layout.html) section of the Guide. For example,
**GUI.Label()** will create a non-interactive label. All the different control
types are explained later, in the [Controls](gui-Controls.html) section of the
Guide.

### Position

The **Position** is the first argument in any **GUI** Control function. The
argument itself is provided with a **Rect()** function. **Rect()** defines
four properties: **left-most position** , **top-most position** , **total
width** , **total height**. All of these values are provided in **integers** ,
which correspond to **pixel** The smallest unit in a computer image. Pixel
size depends on your screen resolution. Pixel lighting is calculated at every
screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) values. All UnityGUI controls work in
**Screen Space** , which is the resolution of the published player in pixels.

The coordinate system is top-left based. **Rect(10, 20, 300, 100)** defines a
Rectangle that starts at coordinates: 10,20 and ends at coordinates 310,120.
It is worth repeating that the second pair of values in **Rect()** are total
width and height, not the coordinates where the controls end. This is why the
example mentioned above ends at 310,120 and not 300,100.

You can use the **Screen.width** and **Screen.height** properties to get the
total dimensions of the screen space available in the player. The following
example may help clarify how this is done:

    
    
    /* Screen.width & Screen.height example */
    using UnityEngine;
    using System.Collections;
    
    public class GUITest : MonoBehaviour 
    {
                
        void OnGUI()
        {
            GUI.Box (new Rect (0,0,100,50), "Top-left");
            GUI.Box (new Rect (Screen.width - 100,0,100,50), "Top-right");
            GUI.Box (new Rect (0,Screen.height - 50,100,50), "Bottom-left");
            GUI.Box (new Rect (Screen.width - 100,Screen.height - 50,100,50), "Bottom-right");
        }
    
    }
    

![The Boxes positioned by the above example](../uploads/Main/gsg-
ScreenWidthHeight.png) The Boxes positioned by the above example

### Content

The second argument for a GUI Control is the actual content to be displayed
with the Control. Most often you will want to display some text or an image on
your Control. To display text, pass a string as the Content argument like
this:

    
    
    using UnityEngine;
    using System.Collections;
    
    public class GUITest : MonoBehaviour 
    {
        void OnGUI ()
        {
            GUI.Label (new Rect (0,0,100,50), "This is the text string for a Label Control");
        }
    }
    

To display an image, declare a **Texture2D** public variable, and pass the
variable name as the content argument like this:

    
    
    /* Texture2D Content example */
    public Texture2D controlTexture;
      ...
    
    void OnGUI () 
    {
        GUI.Label (new Rect (0,0,100,50), controlTexture);
    }
    

Here is an example closer to a real-world scenario:

    
    
    /* Button Content examples */
    using UnityEngine;
    using System.Collections;
    
    public class GUITest : MonoBehaviour
    {
        public Texture2D icon;
        
        void OnGUI () 
        {
            if (GUI.Button (new Rect (10,10, 100, 50), icon)) 
            {
                print ("you clicked the icon");
            }
        
            if (GUI.Button (new Rect (10,70, 100, 20), "This is text")) 
            {
                print ("you clicked the text button");
            }
        }
    }
    

![The Buttons created by the above example](../uploads/Main/gsg-
IconStringContent.png) The Buttons created by the above example

There is a third option which allows you to display images and text together
in a GUI Control. You can provide a **GUIContent** object as the Content
argument, and define the string and image to be displayed within the
GUIContent.

    
    
    /* Using GUIContent to display an image and a string */
    using UnityEngine;
    using System.Collections;
    
    public class GUITest : MonoBehaviour
    {
        public Texture2D icon;
    
        void OnGUI () 
        {
            GUI.Box (new Rect (10,10,100,50), new GUIContent("This is text", icon));
        }
    }
    

You can also define a **Tooltip** in the GUIContent, and display it elsewhere
in the GUI when the mouse hovers over it.

    
    
    /* Using GUIContent to display a tooltip */
    using UnityEngine;
    using System.Collections;
    
    public class GUITest : MonoBehaviour 
    {
        void OnGUI () 
        {
            // This line feeds "This is the tooltip" into GUI.tooltip
            GUI.Button (new Rect (10,10,100,20), new GUIContent ("Click me", "This is the tooltip"));
            
            // This line reads and displays the contents of GUI.tooltip
            GUI.Label (new Rect (10,40,100,20), GUI.tooltip);
        }
    }
    

You can also use GUIContent to display a string, an icon, and a tooltip.

    
    
    /* Using GUIContent to display an image, a string, and a tooltip */
    using UnityEngine;
    using System.Collections;
    
    public class GUITest : MonoBehaviour 
    {
        public Texture2D icon;
        
        void OnGUI () 
        {
            GUI.Button (new Rect (10,10,100,20), new GUIContent ("Click me", icon, "This is the tooltip"));
            GUI.Label (new Rect (10,40,100,20), GUI.tooltip);
        }
    }
    

The script reference page for the [GUIContent
constructor](../ScriptReference/GUIContent-ctor.html) has some examples of its
use.

[](GUIScriptingGuide.html)

Immediate Mode GUI (IMGUI)

[](gui-Controls.html)

IMGUI Controls

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

